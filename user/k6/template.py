pkgname = "k6"
pkgver = "0.55.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Load testing tool"
maintainer = "Gabriel M. Dutra <dmdutra@proton.me>"
license = "AGPL-3.0-only"
url = "https://github.com/grafana/k6"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0b32dfbafc91719bba9ffd149ddfb849270beecf3830e99708b9b6c25bf1b677"
# k6 tests requires network connection
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
