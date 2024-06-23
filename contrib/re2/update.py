url = "https://api.github.com/repos/google/re2/git/refs/tags"
pattern = r"refs/tags/(\d+\-\d+\-\d+)"


def fetch_versions(self, src):
    return map(lambda v: v.replace("-", "."), self.fetch_versions(src))
