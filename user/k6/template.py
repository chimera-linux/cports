pkgname = "k6"
pkgver = "1.4.2"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Load testing tool"
license = "AGPL-3.0-only"
url = "https://github.com/grafana/k6"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1f653584c4b8a191474a55a8f2a1ae661b82c6e7e90e243cf27969eb21ee8453"
# k6 tests requires network connection
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
