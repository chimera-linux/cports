pattern = r"dialog-([\d.-]+)\.tgz"


def fetch_versions(self, src):
    return map(lambda ver: ver.replace("-", "."), self.fetch_versions(src))
