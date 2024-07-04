pkgname = "stress-ng"
pkgver = "0.18.01"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf"]
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
sha256 = "30465ee60a32d9018d0de8a78cfeaa576e869b6e6db87e3628d0704dbe61b561"
env = {
    "MAN_COMPRESS": "0",
    "PRESERVE_CFLAGS": "1",
}
hardening = ["!int"]
# no portable tests defined
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
