pkgname = "bzip3"
pkgver = "1.5.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
]
pkgdesc = "Better and stronger spiritual successor to BZip2"
license = "LGPL-3.0-or-later AND Apache-2.0"
url = "https://github.com/kspalaiologos/bzip3"
source = f"{url}/releases/download/{pkgver}/bzip3-{pkgver}.tar.zst"
sha256 = "d1b9d07dcb0b191c47497da4a52553a7328e0446ae60b1b6981701a21133fae7"


@subpackage("bzip3-libs")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libbzip3")]
    return self.default_libs()


@subpackage("bzip3-devel")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libbzip3-devel")]
    return self.default_devel()
