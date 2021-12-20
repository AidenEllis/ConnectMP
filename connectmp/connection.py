from .settings import DATABASE

__all__ = ['Connection']


class Connection:
    def __init__(self, process_id):
        self.process_id = process_id
        self.database = DATABASE

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
