class DataMatchedException(Exception):
    def __init__(self, data=None):
        self.data = data

    def __str__(self):
        return f"Data Matched! data: {self.data}"
