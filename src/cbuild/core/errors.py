class CbuildException(Exception):
    def __init__(self, msg, extra=None):
        super().__init__(msg)
        self.extra = extra


class TracebackException(Exception):
    pass


class PackageException(Exception):
    def __init__(self, msg, end, pkg, bt=True, quiet=False, hint=None):
        super().__init__(msg)
        self.end = end
        self.pkg = pkg
        self.bt = bt
        self.quiet = quiet
        self.hint = hint
