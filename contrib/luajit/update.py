pattern = r"v2.1-\d+"


def fetch_versions(self, src):
    return map(lambda v: v.replace("-", "_p"), self.fetch_versions(src))
