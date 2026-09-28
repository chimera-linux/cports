def fetch_versions(self, src):
    return map(lambda v: v.replace("alpha", "_alpha"), self.fetch_versions(src))
