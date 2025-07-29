_vver = 20

pattern = r"/tags/([\d.]+-valve\d+)\""
pkgver = f"{self.pkgver}.{_vver}"


def fetch_versions(self, src):
    return map(lambda v: v.replace("-valve", "."), self.fetch_versions(src))
