pkgname = "k6"
pkgver = "1.0.0"
pkgrel = 3
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Load testing tool"
license = "AGPL-3.0-only"
url = "https://github.com/grafana/k6"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "790e8a1d1171262095edbd5df5a74f18406d11ea88098560d0f18b7614c8b880"
# k6 tests requires network connection
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
