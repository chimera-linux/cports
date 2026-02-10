pkgname = "k6"
pkgver = "1.5.0"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Load testing tool"
license = "AGPL-3.0-only"
url = "https://github.com/grafana/k6"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "215f25088ef4a6c52d18e8ee572149c880f1eabf312909e9e87faad5ffe3f00e"
# k6 tests requires network connection
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
