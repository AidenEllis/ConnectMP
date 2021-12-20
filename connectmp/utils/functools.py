import inspect


def accepts_connection_kwarg(func):
    """returns True if the func have either one param 'kwargs' or 'connection' else False"""
    params = list(inspect.signature(func).parameters)
    return 'kwargs' in params or 'connection' in params
