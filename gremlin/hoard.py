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
from gremlin.matrix_math_utils import MatrixMathUtils
from gremlin.database_utils import DatabaseUtils


class Hoard:
    def __init__(self, hoard_file_name=None, hoard_row_size=None):
        self.hoard_file_name = hoard_file_name
        self.hoard = list()
        self.hoard_row_size = hoard_row_size

        self.db = DatabaseUtils(self.hoard_file_name)

        self.init_hoard()
        self.get_hoard()

    # TODO: test
    def init_hoard(self):
        # TODO: check if db exists
        # TODO: check if table exists
        self.db.create_hoard_table()
        # TODO: check if hoard_matrix tag exists
        hoard_tag = self.db.get_by_tag("hoard")
        # TODO: check if hoard_matrix tag returns hoard matrix blob
        hoard_tag.
        pass

    def get_hoard(self):
        hoard_array_size = self.hoard_row_size * self.hoard_row_size
        # TODO: set up tag to tag hoard matrix
        hoard_string = self.db.get_by_tag("hoard_matrix")
        self.hoard = BinaryFileUtils.string_to_bits(hoard_string, length=hoard_array_size)

    def get_cell(self, hoard_row, hoard_column):
        hoard_cell_index = MatrixMathUtils.get_cell_index(hoard_row, hoard_column, self.hoard_row_size)
        return self.hoard[hoard_cell_index]

    def get_row(self, hoard_row):
        hoard_row_indexes = MatrixMathUtils.get_row_indexes(hoard_row, self.hoard_row_size)
        return [self.hoard[i] for i in hoard_row_indexes]

    def get_rows(self, hoard_row_indexes):
        hoard_rows = list()
        for i in hoard_row_indexes:
            row = self.get_row(i)
            hoard_rows.append(row)
        return hoard_rows

    def get_column(self, hoard_column):
        hoard_column_indexes = MatrixMathUtils.get_column_indexes(hoard_column, self.hoard_row_size)
        return [self.hoard[i] for i in hoard_column_indexes]

    def get_riddled_row(self, hoard_row, riddle_column_indexes):
        riddled_row_indexes = MatrixMathUtils.get_columns_in_row(hoard_row, riddle_column_indexes, self.hoard_row_size)
        return [self.hoard[i] for i in riddled_row_indexes]

    # TODO: test
    def add_row(self, row_string):
        """Add row and respective column
        by appending row string to end of hoard array
        and inserting 0s at hoard_row_size column index
        """
        new_row = BinaryFileUtils.string_to_bits(row_string)
        for cell in new_row:
            self.hoard.append(cell)
        hoard_column_indexes = MatrixMathUtils.get_column_indexes(self.hoard_row_size, self.hoard_row_size)
        [self.hoard.insert(i, 0) for i in hoard_column_indexes]

    # TODO: test
    def add_tags(self, row_index, tag_indexes):
        """Add tags to row
        by setting row's tag indexes to 1s
        """
        cell_indexes = MatrixMathUtils.get_columns_in_row(row_index, tag_indexes, self.hoard_row_size)
        [self.hoard.insert(i, 1) for i in cell_indexes]

    # TODO: test
    def remove_tags(self, row_index, tag_indexes):
        """Remove tags from row
        by setting row's tag indexes to 0s
        """
        cell_indexes = MatrixMathUtils.get_columns_in_row(row_index, tag_indexes, self.hoard_row_size)
        [self.hoard.insert(i, 0) for i in cell_indexes]

    # TODO: test
    def remove_row(self, row_index):
        """Removes row and respective column
        by removing cells at row_index row
        and removing cells at row_index column
        """
        row_column_indexes = MatrixMathUtils.get_column_indexes(row_index, self.hoard_row_size)
        [self.hoard.remove(i) for i in row_column_indexes]
        row_indexes = MatrixMathUtils.get_row_indexes(row_index, self.hoard_row_size)
        [self.hoard.remove(i) for i in row_indexes]
