pattern = r"releases/tag/([0-9\-]+)"


def fetch_versions(self, url):
    return map(lambda v: v.replace("-", "."), self.fetch_versions(url))
