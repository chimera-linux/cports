pattern = r"cryptsetup\ Debian\ release\ 2:([\d.\-~rc]+)"
ignore = ["*rc*", "*~*"]


def fetch_versions(self, src):
    return map(lambda v: v.replace("-", "."), self.fetch_versions(src))
