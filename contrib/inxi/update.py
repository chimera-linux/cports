url = "https://codeberg.org/smxi/inxi/tags"
pattern = r">(\d+\.\d+\.\d+\-\d+)<"


def fetch_versions(self, src):
    return map(lambda v: v.replace("-", "."), self.fetch_versions(src))
