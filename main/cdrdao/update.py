url = "https://github.com/cdrdao/cdrdao/tags.atom"
pattern = r"tag/rel_([\d_]+)\""


def fetch_versions(self, src):
    return map(lambda v: v.replace("_", "."), self.fetch_versions(src))
