pkgname = "hashcat"
pkgver = "6.2.6"
pkgrel = 0
build_style = "makefile"
make_env = {
    "PREFIX": "/usr",
    "SED": "/usr/bin/gsed",
    "USE_SYSTEM_ZLIB": "1",
    "USE_SYSTEM_OPENCL": "1",
    "USE_SYSTEM_XXHASH": "1",
}
make_use_env = True
hostmakedepends = ["gsed"]
makedepends = [
    "linux-headers",
    "minizip-devel",
    "opencl-headers",
    "xxhash-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Password recovery tool"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "MIT"
url = "https://hashcat.net/hashcat"
source = f"https://hashcat.net/files/hashcat-{pkgver}.tar.gz"
sha256 = "b25e1077bcf34908cc8f18c1a69a2ec98b047b2cbcf0f51144dcf3ba1e0b7b2a"
# check: no obvious test suite
options = ["!check"]


if self.profile().endian == "big":
    broken = "bug endian"


def post_install(self):
    self.install_license("docs/license.txt")
