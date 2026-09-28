url = "https://github.com/rust-lang/rust-analyzer"
pattern_style = "git_forge"
pattern = r"refs/tags/(\d+\-\d+\-\d+)"
ignore = ["nightly"]


def fetch_versions(self, src):
    return map(lambda v: v.replace("-", "."), self.fetch_versions(src))
