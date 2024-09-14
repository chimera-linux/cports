pattern = r"(\d+_\d+_\d+).[A-z0-9]+.tar.zst"
url = "https://passt.top/passt/refs/tags"


def fetch_versions(self, src):
    return map(lambda v: v.replace("_", "."), self.fetch_versions(src))
