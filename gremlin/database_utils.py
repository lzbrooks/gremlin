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

import sqlite3


class DatabaseUtils:
    def __init__(self, hoard_file_name=None):
        if not hoard_file_name:
            self.hoard_file_name = 'hoard.db'
        else:
            self.hoard_file_name = hoard_file_name
        self.connect_database()

    # TODO: test
    def connect_database(self):
        self.conn = sqlite3.connect(self.hoard_file_name)
        self.c = self.conn.cursor()
        return self.c

    # TODO: test
    def create_hoard_table(self):
        self.c.execute("CREATE TABLE hoard (content_hash text, tag blob)")
        self.conn.commit()

    # TODO: test
    def insert_tags(self, new_tags):
        # new_tag = [(hash_string, new_binary), ...]
        self.c.executemany('INSERT INTO hoard VALUES (?,?)', new_tags)
        self.conn.commit()

    # TODO: test
    def get_by_tag(self, tag):
        # tag = (tag,)
        self.c.execute('SELECT * FROM hoard WHERE tag=?', tag)
        print(c.fetchall())

    # TODO: test
    def get_by_hash(self, hash_string):
        # hash_string = (hash_string,)
        self.c.execute('SELECT * FROM hoard WHERE content_hash=?', hash_string)
        print(c.fetchall())

    # TODO: test
    def close_database_connection(self):
        self.conn.close()
