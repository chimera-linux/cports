pkgname = "stress-ng"
pkgver = "0.18.10"
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
sha256 = "bb729844b5a3c8953e58ddb705dce8a62078ad75f0b6f49092f8027d9c699700"
env = {
    "MAN_COMPRESS": "0",
    "PRESERVE_CFLAGS": "1",
}
hardening = ["!int"]
# no portable tests defined
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
