pkgname = "yara"
pkgver = "4.5.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-cuckoo",
    "--enable-dex",
    "--enable-magic",
]
hostmakedepends = [
    "automake",
    "flex",
    "libtool",
    "pkgconf",
]
makedepends = [
    "file-devel",
    "jansson-devel",
    "linux-headers",
    "openssl3-devel",
]
pkgdesc = "C library for pattern matching"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://virustotal.github.io/yara"
source = (
    f"https://github.com/VirusTotal/yara/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "1f87056fcb10ee361936ee7b0548444f7974612ebb0e681734d8de7df055d1ec"


def post_install(self):
    self.install_license("COPYING")


@subpackage("yara-devel")
def _(self):
    return self.default_devel()
