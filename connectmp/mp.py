import uuid
from .settings import DATABASE
from .connection import Connection
from multiprocessing import Process as MProcess
from .utils.functools import accepts_connection_kwarg


class Process(MProcess):

    def __init__(self, target, connection=False, conn_var='connection', args: tuple = None, kwargs: dict = None):
        if not kwargs:
            kwargs = {}
        if not args:
            args = ()

        self.process_id = str(uuid.uuid4())
        if connection:
            self.connection = Connection(self.process_id)
            DATABASE.createObj(self.process_id)
        if connection and target:
            if accepts_connection_kwarg(target):
                kwargs[conn_var] = self.connection
        MProcess.__init__(self, target=target, args=args, kwargs=kwargs)
