pattern = r"munt_([0-9_]+)"


def fetch_versions(self, src):
    return map(lambda v: v.replace("_", "."), self.fetch_versions(src))
