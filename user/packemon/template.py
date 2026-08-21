pkgname = "packemon"
pkgver = "1.8.26"
pkgrel = 1
build_style = "go"
make_build_args = ["./cmd/packemon"]
hostmakedepends = ["go"]
depends = ["iproute2"]
pkgdesc = "TUI network packet generator and monitor"
license = "BSD-2-Clause"
url = "https://github.com/ddddddO/packemon"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "dabfcb37057090dbe54f12a9700f86504c059f4e4d8a28eab44c5a90fe679801"
# check: needs network
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
