pkgname = "stress-ng"
pkgver = "0.18.04"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["pkgconf"]
makedepends = [
    "acl-devel",
    "libjpeg-turbo-devel",
    "linux-headers",
    "xxhash-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Stress test a computer in various selectable ways"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/ColinIanKing/stress-ng"
source = f"https://github.com/ColinIanKing/stress-ng/archive/refs/tags/V{pkgver}.tar.gz"
sha256 = "c76cf067e582fb8a066d47207bbccc6d0d4175ba700b5d122909132d79e7f6ea"
env = {
    "MAN_COMPRESS": "0",
    "PRESERVE_CFLAGS": "1",
}
hardening = ["!int"]
# no portable tests defined
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
