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

from bitstring import Bits, ConstBitArray


class BinaryFileUtils:
    def __init__(self):
        pass

    @staticmethod
    def string_to_bits(binary_string, length=None):
        return Bits(length=length, bin=binary_string)

    @staticmethod
    def string_to_file(output_file_path, binary_string):
        output_file = open(output_file_path, 'wb')
        Bits(bin=binary_string).tofile(output_file)

    @staticmethod
    def file_to_stream(filename, length=None):
        return ConstBitArray(length=length, filename=filename)
