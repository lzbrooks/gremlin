#  Copyright (C) 2020. Lizann Brooks
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, version 3 of the License.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>

from gremlin.binary_file_utils import BinaryFileUtils
from gremlin.hoard import Hoard
from gremlin.riddle import Riddle


class Gremlin:
    def __init__(self,
                 hoard_file_name=None,
                 riddle_rows_output_file_name=None,
                 hoard_row_size=None):
        self.hoard_row_size = hoard_row_size
        self.hoard = Hoard(hoard_file_name=hoard_file_name, hoard_row_size=hoard_row_size)
        self.riddle = Riddle(hoard_row_size=hoard_row_size)
        self.riddle_rows_output_file_name = riddle_rows_output_file_name

    # TODO: test
    def add_row(self, row_string):
        """Add row and respective column"""
        self.hoard.add_row(row_string)

    # TODO: test
    def add_tags(self, row_index, tag_indexes):
        """Add tags to row"""
        self.hoard.add_tags(row_index, tag_indexes)

    # TODO: test
    def remove_tags(self, row_index, tag_indexes):
        """Remove tags from row"""
        self.hoard.remove_tags(row_index, tag_indexes)

    # TODO: test
    def remove_row(self, row_index):
        """Removes row and respective column"""
        self.hoard.remove_row(row_index)

    def what_am_i(self, riddle, riddle_columns):
        self.riddle.i_am(riddle, riddle_columns)
        resultant_hoard = self.get_resultant_hoard()
        riddle_row_indexes = self.get_riddle_row_indexes(resultant_hoard)
        riddle_rows = self.get_hoard_riddle_rows(riddle_row_indexes)
        self.output_hoard_riddle_rows_to_file(riddle_rows)
        return riddle_rows

    def get_resultant_hoard(self):
        resultant_hoard = list()
        for y in range(self.hoard_row_size):
            riddled_row = self.hoard.get_riddled_row(y, self.riddle.riddle_column_indexes)
            resultant_row = self.get_resultant_row(riddled_row)
            resultant_hoard.append(resultant_row)
        return resultant_hoard

    def get_resultant_row(self, riddled_row):
        resultant_row = list()
        for x in range(len(riddled_row)):
            resultant_cell = self.get_resultant_cell(riddled_row[x], self.riddle.riddle[x])
            resultant_row.append(resultant_cell)
        return resultant_row

    @staticmethod
    def get_resultant_cell(hoard_cell, riddle_cell):
        return ~(hoard_cell ^ riddle_cell)

    def get_riddle_row_indexes(self, resultant_hoard):
        riddle_row_indexes = list()
        for i, resultant_row in resultant_hoard:
            if sum(resultant_row) == len(self.riddle.riddle):
                riddle_row_indexes.append(i)
        return riddle_row_indexes

    def get_hoard_riddle_rows(self, hoard_riddle_indexes):
        return self.hoard.get_rows(hoard_riddle_indexes)

    def output_hoard_riddle_rows_to_file(self, riddle_rows):
        riddle_rows_string = ''.join(riddle_rows)
        BinaryFileUtils.string_to_file(self.riddle_rows_output_file_name, riddle_rows_string)
