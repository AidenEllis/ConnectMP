import uuid
from .settings import DATABASE

__all__ = ['Connection']


class Connection:
    def __init__(self, process_id: str = None):
        self.process_id = process_id
        self.database = DATABASE
        if not self.process_id:
            # Class is being used seperately outside connectmp.
            self.process_id = str(uuid.uuid4())
            self.database.createObj(self.process_id)

    def __getattr__(self, item):
        if item == 'data':
            return self.database.getData(self.process_id)
        else:
            return self.__getattribute__(item)

    def __setattr__(self, key, value):
        if key == 'data':
            self.database.updateData(self.process_id, data=value)
        else:
            super(Connection, self).__setattr__(key, value)
