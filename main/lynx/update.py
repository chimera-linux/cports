def fetch_versions(self, src):
    return map(lambda v: v.replace("dev.", "_pre"), self.fetch_versions(src))
