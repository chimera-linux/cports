url = "https://salsa.debian.org/cryptsetup-team/cryptsetup/-/tags"
pattern = r"cryptsetup\ Debian\ release\ 2:([\d.-]+)"

def fetch_versions(self, src):
    return map(lambda v: v.replace("-", "."), self.fetch_versions(src))
