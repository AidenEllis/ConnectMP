import os
import sqlite3
from pathlib import Path
import _pickle as cpickle
from pickle import HIGHEST_PROTOCOL

__all__ = ['ProcessDatabase']


class ProcessDatabase:
    data_folder = os.path.join(Path(__file__).resolve().parent, 'data')
    if not os.path.exists(data_folder):
        os.mkdir(data_folder)

    db_path = os.path.join(Path(__file__).resolve().parent, 'data', 'database.sqlite3')

    if os.path.exists(db_path):
        try:
            os.remove(db_path)
        except PermissionError:
            pass

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    def __init__(self):
        self.schema = {'process_id': 0, 'data': 1}
        self.initialize_db()

    def initialize_db(self):
        with self.connection:
            try:
                self.cursor.execute("""
                    CREATE TABLE ProcessDatas (
                        process_id TEXT,
                        data BLOB
                    )""")

            except sqlite3.OperationalError:
                pass

    def createObj(self, process_id: str):
        with self.connection:
            values = {
                'process_id': process_id,
                'data': ''
            }
            process_data_exists = list(self.cursor.execute("SELECT * FROM ProcessDatas WHERE process_id=:process_id",
                                                           {'process_id': process_id}).fetchall())

            if not process_data_exists:
                self.cursor.execute("INSERT INTO ProcessDatas VALUES (:process_id, :data)", values)

    def updateData(self, process_id: str, data):
        with self.connection:
            process_data_exists = list(self.cursor.execute("SELECT * FROM ProcessDatas WHERE process_id=:process_id",
                                                           {'process_id': process_id}).fetchall())
            if process_data_exists:
                pickled_data = cpickle.dumps(data, HIGHEST_PROTOCOL)
                self.cursor.execute("UPDATE ProcessDatas SET data=:data WHERE process_id = :process_id",
                                    {'process_id': process_id, 'data': sqlite3.Binary(pickled_data)})

    def getData(self, process_id: str, no_data_default=None):
        with self.connection:
            process_data_exists = list(self.cursor.execute("SELECT * FROM ProcessDatas WHERE process_id=:process_id",
                                                           {'process_id': process_id}).fetchall())

            if process_data_exists:
                pickled_data = process_data_exists[0][self.schema['data']]
                if pickled_data:
                    return cpickle.loads(pickled_data)
                return no_data_default

    def getAllData(self):
        with self.connection:
            result = list(self.cursor.execute("SELECT * FROM ProcessDatas").fetchall())
            return result

    def destroyDB(self):
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
