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


class MatrixMathUtils:
    def __init__(self):
        pass

    @staticmethod
    def get_cell_index(row_index, column_index, matrix_row_size):
        return row_index + column_index * matrix_row_size

    # TODO: test
    @staticmethod
    def get_row_indexes(row_index, matrix_row_size):
        row_indexes = []
        for i in range(matrix_row_size):
            row_indexes.append(row_index + i * matrix_row_size)
        return row_indexes

    # TODO: test
    @staticmethod
    def get_column_indexes(column_index, matrix_row_size):
        column_indexes = []
        for i in range(matrix_row_size):
            column_indexes.append(i + column_index * matrix_row_size)
        return column_indexes

    # TODO: test
    @staticmethod
    def get_columns_in_row(row_index, column_indexes, matrix_row_size):
        cell_indexes = []
        for column_index in column_indexes:
            cell_index = MatrixMathUtils.get_cell_index(row_index, column_index, matrix_row_size)
            cell_indexes.append(cell_index)
        return cell_indexes

    # TODO: test
    @staticmethod
    def get_rows_in_column(row_indexes, column_index, matrix_row_size):
        cell_indexes = []
        for row_index in row_indexes:
            cell_index = MatrixMathUtils.get_cell_index(row_index, column_index, matrix_row_size)
            cell_indexes.append(cell_index)
        return cell_indexes
