url = "https://www.boost.org/users/download"
pattern = r">boost_([\d_]+).tar.bz2<"


def fetch_versions(self, src):
    return map(lambda v: v.replace("_", "."), self.fetch_versions(src))
