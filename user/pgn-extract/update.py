pattern = r"/pgn-extract-(\d\d-\d\d)"


def fetch_versions(self, src):
    return map(lambda v: v.replace("-", "."), self.fetch_versions(src))
