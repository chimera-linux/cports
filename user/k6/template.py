pkgname = "k6"
pkgver = "0.56.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Load testing tool"
maintainer = "Gabriel M. Dutra <dmdutra@proton.me>"
license = "AGPL-3.0-only"
url = "https://github.com/grafana/k6"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a11776d57e9cf3fb306c4f0df9141f972c1b6506c47a750fd71d0f5b24945272"
# k6 tests requires network connection
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
