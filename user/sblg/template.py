pkgname = "sblg"
pkgver = "0.6.1"
pkgrel = 0
build_style = "configure"
configure_args = ["PREFIX=/usr", "MANDIR=/usr/share/man"]
make_cmd = "bmake"
make_check_target = "regress"
hostmakedepends = ["bmake"]
makedepends = ["libexpat-devel"]
checkdepends = ["jq", "valgrind"]
pkgdesc = "Static site generator"
license = "ISC"
url = "https://kristaps.bsd.lv/sblg"
source = f"https://github.com/kristapsdz/sblg/archive/refs/tags/VERSION_{pkgver.replace('.', '_')}.tar.gz"
sha256 = "f5db8c1fed5276aa90e58eea53c3cbe5e81f123057240191a8fc86a8404627d3"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE.md")
