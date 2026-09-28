pattern = r">([\d.-]+)<"
ignore = ["1*", ".", "[6789][0-9]"]


def fetch_versions(self, src):
    return map(lambda v: v.replace("-", "."), self.fetch_versions(src))
