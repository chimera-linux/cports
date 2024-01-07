pattern = r"cryptsetup\ Debian\ release\ 2:([\d.-]+)"


def fetch_versions(self, src):
    return map(lambda v: v.replace("-", "."), self.fetch_versions(src))
