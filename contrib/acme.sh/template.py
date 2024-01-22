pkgname = "acme.sh"
pkgver = "3.0.7"
pkgrel = 0
depends = ["curl", "openssl", "socat"]
pkgdesc = "ACME Shell script"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-3.0-only"
url = "https://github.com/acmesh-official/acme.sh"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "abd446d6bd45d0b44dca1dcbd931348797a3f82d1ed6fb171472eaf851a8d849"


def do_install(self):
    self.install_files("deploy", "usr/share/acme.sh")
    self.install_files("dnsapi", "usr/share/acme.sh")
    self.install_files("notify", "usr/share/acme.sh")

    self.install_bin("acme.sh")


def post_install(self):
    self.install_license("LICENSE.md")
