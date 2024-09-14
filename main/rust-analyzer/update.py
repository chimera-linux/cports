url = "https://api.github.com/repos/rust-lang/rust-analyzer/git/refs/tags"
pattern = r"refs/tags/(\d+\-\d+\-\d+)"
ignore = ["nightly"]


def fetch_versions(self, src):
    return map(lambda v: v.replace("-", "."), self.fetch_versions(src))
