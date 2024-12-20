pkgname = "bzip3"
pkgver = "1.5.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
]
pkgdesc = "Better and stronger spiritual successor to BZip2"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-3.0-or-later AND Apache-2.0"
url = "https://github.com/kspalaiologos/bzip3"
source = f"{url}/releases/download/{pkgver}/bzip3-{pkgver}.tar.zst"
sha256 = "6223fc69a0e983712242d225930b212879454b81eb2712f5f8d9cda3a69b08e1"
hardening = ["vis", "cfi"]


@subpackage("libbzip3")
def _(self):
    return self.default_libs()


@subpackage("libbzip3-devel")
def _(self):
    return self.default_devel()
