def fetch_versions(self, src):
    return map(lambda v: v.replace(".beta", "_beta"), self.fetch_versions(src))
