url = "https://ftp.gnu.org/gnu/xorriso"


def fetch_versions(self, src):
    return map(lambda v: v.replace(".pl0", "."), self.fetch_versions(src))
