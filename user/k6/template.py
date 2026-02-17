pkgname = "k6"
pkgver = "1.6.1"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Load testing tool"
license = "AGPL-3.0-only"
url = "https://github.com/grafana/k6"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3a6948ebfe9bc5fc19dfd0f7ec7d39737c8d702c35cfc457ad53da179e9dcb90"
# k6 tests requires network connection
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
