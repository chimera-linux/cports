def fetch_versions(self, src):
    return map(lambda v: v.replace("p", "_p"), self.fetch_versions(src))
