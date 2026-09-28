pkgname = "CUnit"
pattern = r"/CUnit-([0-9\-\.]+).tar.bz2"


def fetch_versions(self, src):
    return map(lambda v: v.replace("-", "."), self.fetch_versions(src))
