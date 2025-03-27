pkgname = "Algorithm-Diff"


def fixversion(v):
    major, minor = v.rsplit(".", 1)
    minor_zeroed = minor.ljust(4, "0")
    return f"{major}.{minor_zeroed}"


def fetch_versions(self, src):
    return map(fixversion, self.fetch_versions(src))


pkgver = fixversion(self.pkgver)
