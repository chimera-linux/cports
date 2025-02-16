url = "https://api.github.com/repos/kristapsdz/sblg/git/refs/tags"
pattern = r"refs/tags/VERSION_([\d\_]+)\""


def fetch_versions(self, src):
    return map(lambda v: v.replace("_", "."), self.fetch_versions(src))
