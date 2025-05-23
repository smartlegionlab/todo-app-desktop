# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024-2025, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import sqlite3


class Database:
    def __init__(self, db_name='tasks.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                uuid TEXT NOT NULL UNIQUE,
                name TEXT NOT NULL,
                completed BOOLEAN NOT NULL
            )
        ''')
        self.conn.commit()

    def add_task(self, uuid, name):
        self.cursor.execute('INSERT INTO tasks (uuid, name, completed) VALUES (?, ?, ?)',
                            (uuid, name, False))
        self.conn.commit()

    def update_task(self, uuid, name, completed):
        self.cursor.execute('UPDATE tasks SET name = ?, completed = ? WHERE uuid = ?',
                            (name, int(completed), uuid))
        self.conn.commit()

    def delete_task(self, uuid):
        self.cursor.execute('DELETE FROM tasks WHERE uuid = ?', (uuid,))
        self.conn.commit()

    def get_all_tasks(self):
        self.cursor.execute('SELECT uuid, name, completed FROM tasks')
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
