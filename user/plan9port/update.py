url = "https://github.com/9fans/plan9port/commits/master.atom"
pattern = r"<updated>(\d\d\d\d-\d\d-\d\d)T"  # YYYY-mm-dd


def fetch_versions(self, src):
    return map(lambda v: "0_git" + v.replace("-", ""), self.fetch_versions(src))
