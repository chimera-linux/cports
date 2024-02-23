_vver = 17

pattern = r"/tags/([\d.]+-valve\d+)"
pkgver = f"{self.pkgver}.{_vver}"
ignore = ["6.1.61.*"]


def fetch_versions(self, src):
    return map(lambda v: v.replace("-valve", "."), self.fetch_versions(src))
