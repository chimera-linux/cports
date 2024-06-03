url = "https://github.com/vancegroup/freealut/tags"
pattern = r"freealut_([\d\_]+).tar.gz"


def fetch_versions(self, src):
    return map(lambda v: v.replace("_", "."), self.fetch_versions(src))
