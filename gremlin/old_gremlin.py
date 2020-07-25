from bitstring import ConstBitArray, Bits


class Gremlin:
    def __init__(self):
        self.hoard_file_name = 'test/hoard'
        self.hoard_file_stream = [True, True, True, False, True, False, False, True, True]
        self.hoard_file_row_size = 3
        self.riddle_file_name = 'test/riddle'
        self.riddle_input_stream = [True, False, True]
        self.riddle_columns_file_name = 'test/riddle_columns'
        self.riddle_columns_stream = [True, True, True]
        self.hoard_riddle_output_file_name = 'test/hoard_riddle_output'

        self.hoard = []

        self.riddle = []
        self.riddle_matrix = []
        self.riddle_columns = []
        self.riddle_column_indexes = []

        self.resultant_hoard = []
        self.hoard_riddle_indexes = []
        self.hoard_riddle_rows = []

    def get_hoard(self):
        # self.hoard_file_stream = Bits(filename=self.hoard_file_name)
        # for row in self.hoard_file_stream.cut(self.hoard_file_row_size):
        #     self.hoard.append(row)
        self.hoard = ConstBitArray(filename=self.hoard_file_name)

    def get_hoard_cell(self, hoard_row, hoard_column):
        return self.hoard[hoard_row + hoard_column * self.hoard_file_row_size]

    def get_hoard_row(self, hoard_row):
        hoard_row_indexes = []
        for i in range(self.hoard_file_row_size):
            hoard_row_indexes = hoard_row + i * self.hoard_file_row_size
        return [self.hoard[i] for i in hoard_row_indexes]

    def get_hoard_column(self, hoard_column):
        hoard_column_indexes = []
        for i in range(self.hoard_file_row_size):
            hoard_column_indexes = i + hoard_column * self.hoard_file_row_size
        return [self.hoard[i] for i in hoard_column_indexes]

    def get_riddled_row(self, hoard_row):
        hoard_riddled_column_indexes = []
        for i in self.riddle_column_indexes:
            hoard_riddled_column_indexes = hoard_row + i * self.hoard_file_row_size
        return [self.hoard[i] for i in hoard_riddled_column_indexes]

    def get_riddle(self):
        self.riddle = ConstBitArray(filename=self.riddle_file_name)

    def get_riddle_columns(self):
        self.riddle_columns_stream = ConstBitArray(filename=self.riddle_columns_file_name)
        # self.riddle_column_indexes = map(self.riddle_columns_stream, range(self.hoard_file_row_size))
        for i in range(self.hoard_file_row_size):
            if self.riddle_columns_stream[i]:
                self.riddle_column_indexes.append(i)

    def get_resultant_hoard(self):
        for y in range(self.hoard_file_row_size):
            hoard_riddled_row = self.get_riddled_row(y)
            # hoard_resultant_row = ~(hoard_riddled_row ^ self.riddle)
            # self.resultant_hoard.append(hoard_resultant_row)
            hoard_resultant_row = []
            for x in range(len(hoard_riddled_row)):
                hoard_resultant_cell = ~(hoard_riddled_row[x] ^ self.riddle[x])
                hoard_resultant_row.append(hoard_resultant_cell)
            self.resultant_hoard.append(hoard_resultant_row)

    def get_hoard_riddle_indexes(self):
        for i, resultant_row in self.resultant_hoard:
            if sum(resultant_row) == 3:
                self.hoard_riddle_indexes.append(i)

    def get_hoard_riddle_rows(self):
        for i in self.hoard_riddle_indexes:
            riddle_row = self.get_hoard_row(i)
            self.hoard_riddle_rows.append(riddle_row)

    def output_hoard_riddle_rows(self):
        hoard_riddle_output_file = open(self.hoard_riddle_output_file_name, 'wb')
        hoard_riddle_string = ''.join(self.hoard_riddle_rows)
        Bits(bin=hoard_riddle_string).tofile(hoard_riddle_output_file)

    def i_am(self):
        self.get_riddle()
        self.get_riddle_columns()

    def what_am_i(self):
        self.get_resultant_hoard()
        self.get_hoard_riddle_indexes()
        self.get_hoard_riddle_rows()

    def riddles_in_the_dark(self):
        self.i_am()
        self.what_am_i()
