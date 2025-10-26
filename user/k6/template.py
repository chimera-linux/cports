pkgname = "k6"
pkgver = "1.3.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Load testing tool"
license = "AGPL-3.0-only"
url = "https://github.com/grafana/k6"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6a04403eea25fc721de3a7515b89301fb8679deb3faff5c9703d79d76e114fd9"
# k6 tests requires network connection
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
