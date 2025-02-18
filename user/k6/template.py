pkgname = "k6"
pkgver = "0.57.0"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Load testing tool"
maintainer = "Gabriel M. Dutra <dmdutra@proton.me>"
license = "AGPL-3.0-only"
url = "https://github.com/grafana/k6"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "75ccb3f7a9d3c2045d71b9bbb37d8a5e1b482b374d5c3deedac4523700a5bf05"
# k6 tests requires network connection
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
