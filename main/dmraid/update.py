pattern = r"dmraid-([\d.rc]+)-\d+\.tar.bz2"


def fetch_versions(self, src):
    return map(lambda v: v.replace(".rc", "_rc"), self.fetch_versions(src))
