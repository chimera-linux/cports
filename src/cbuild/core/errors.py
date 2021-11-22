class CbuildException(Exception):
    def __init__(self, msg, extra = None):
        super().__init__(msg)
        self.extra = extra
