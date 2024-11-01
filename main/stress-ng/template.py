pkgname = "stress-ng"
pkgver = "0.18.06"
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
sha256 = "f3197c010b1ac23b015a6f8e8c84a24cee02750bf41a1527379ccb31ca4f889a"
env = {
    "MAN_COMPRESS": "0",
    "PRESERVE_CFLAGS": "1",
}
hardening = ["!int"]
# no portable tests defined
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
