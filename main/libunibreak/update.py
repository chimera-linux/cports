pattern = r"libunibreak_([\d\_]+).tar.gz"


def fetch_versions(self, src):
    return map(lambda v: v.replace("_", "."), self.fetch_versions(src))
