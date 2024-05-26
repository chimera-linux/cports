_vver = 7

pattern = r"/tags/([\d.]+-valve\d+)"
pkgver = f"{self.pkgver}.{_vver}"
ignore = ["6.8.*"]


def fetch_versions(self, src):
    return map(lambda v: v.replace("-valve", "."), self.fetch_versions(src))
