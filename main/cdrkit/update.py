pattern = r"%25([\d.-]+)</id>"


def fetch_versions(self, src):
    return map(lambda v: v.replace("-", "."), self.fetch_versions(src))
