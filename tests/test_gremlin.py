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

# import pytest
# from gremlin.hoard import Hoard
# from gremlin.riddle import Riddle


def test_gremlin_with_valid_values(valid_gremlin):
    assert valid_gremlin.hoard.hoard.bin == "111010011"
    assert valid_gremlin.riddle.riddle.bin == "101"
    assert valid_gremlin.hoard.hoard_file_row_size == 3
    # assert valid_gremlin.hoard == Hoard(hoard_file_name=hoard_file_name, hoard_file_row_size=hoard_file_row_size)
    # assert valid_gremlin.riddle == Riddle(riddle_file_name=riddle_file_name,
    # riddle_columns_file_name=riddle_columns_file_name, hoard_file_row_size=hoard_file_row_size)
    # hoard_riddle_output_file_name = hoard_riddle_output_file_name
    assert not valid_gremlin.resultant_hoard
    assert not valid_gremlin.hoard_riddle_indexes
    assert not valid_gremlin.hoard_riddle_rows
    assert valid_gremlin.riddle.riddle_columns_stream.bin == "111"
    assert valid_gremlin.riddle.riddle_column_indexes == [0, 1, 2]
