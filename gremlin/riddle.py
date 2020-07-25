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


class Riddle:
    def __init__(self, hoard_row_size=None):
        self.riddle = list()
        self.riddle_columns = list()
        self.hoard_row_size = hoard_row_size
        self.riddle_column_indexes = list()

    def i_am(self, riddle, riddle_columns):
        self.get_riddle(riddle)
        self.get_riddle_columns(riddle_columns)
        self.get_riddle_column_indexes()

    def get_riddle(self, riddle):
        self.riddle = BinaryFileUtils.string_to_bits(riddle)

    def get_riddle_columns(self, riddle_columns):
        self.riddle_columns = BinaryFileUtils.string_to_bits(riddle_columns)

    def get_riddle_column_indexes(self):
        for i in range(self.hoard_row_size):
            if self.riddle_columns[i]:
                self.riddle_column_indexes.append(i)
