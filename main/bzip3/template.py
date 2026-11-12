pkgname = "bzip3"
pkgver = "1.5.5"
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
sha256 = "26e0eaf81668219727cc25529337277e87df989174b555a8ecc5ce61b95e76e0"


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
