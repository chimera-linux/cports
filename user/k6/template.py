pkgname = "k6"
pkgver = "0.58.0"
pkgrel = 2
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Load testing tool"
license = "AGPL-3.0-only"
url = "https://github.com/grafana/k6"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "013c5deb43264afc2f17a2f059fa27a706464abb235af401acfda26bb45fd8e7"
# k6 tests requires network connection
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
