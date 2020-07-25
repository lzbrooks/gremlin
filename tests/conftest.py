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
import os

import pytest

from gremlin.gremlin import Gremlin


@pytest.fixture
def valid_file_paths():
    test_directory = os.path.dirname(__file__)
    dummy_data_directory = os.path.join(test_directory, 'dummy_data')
    hoard_file_path = os.path.join(dummy_data_directory, 'hoard')
    riddle_file_name = os.path.join(dummy_data_directory, 'riddle')
    riddle_columns_file_name = os.path.join(dummy_data_directory, 'riddle_columns')
    hoard_riddle_output_file_name = os.path.join(dummy_data_directory, 'output_hoard')
    valid_file_paths = {
        "hoard_file_path": hoard_file_path,
        "riddle_file_name": riddle_file_name,
        "riddle_columns_file_name": riddle_columns_file_name,
        "hoard_riddle_output_file_name": hoard_riddle_output_file_name
    }
    return valid_file_paths


@pytest.fixture
def valid_gremlin(valid_file_paths):
    valid_gremlin = Gremlin(hoard_file_name=valid_file_paths.get("hoard_file_path"),
                            riddle_file_name=valid_file_paths.get("riddle_file_name"),
                            riddle_columns_file_name=valid_file_paths.get("riddle_columns_file_name"),
                            hoard_riddle_output_file_name=valid_file_paths.get("hoard_riddle_output_file_name"),
                            hoard_row_size=3)
    return valid_gremlin
