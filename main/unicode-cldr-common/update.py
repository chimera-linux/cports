url = "https://api.github.com/repos/unicode-org/cldr/git/refs/tags"
pattern = r"refs/tags/release-([\d-]+)\""


def fetch_versions(self, src):
    return map(lambda v: v.replace("-", "."), self.fetch_versions(src))
