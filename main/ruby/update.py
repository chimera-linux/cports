url = "https://api.github.com/repos/ruby/ruby/git/refs/tags"
pattern = r"refs/tags/v(\d+\_\d+\_\d+)\""


def fetch_versions(self, src):
    return map(lambda v: v.replace("_", "."), self.fetch_versions(src))
