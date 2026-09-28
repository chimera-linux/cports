pkgname = "libde265"
pkgver = "1.1.3"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Open H.265 codec implementation"
license = "LGPL-3.0-or-later"
url = "http://www.libde265.org"
source = f"https://github.com/strukturag/libde265/archive/v{pkgver}.tar.gz"
sha256 = "189baa08fd6d2dd34db099de411bd6b2e6bd5eb88e81236a3d0fa3826b9715c4"
# no tests
options = ["!check"]


@subpackage("libde265-devel")
def _(self):
    return self.default_devel()


@subpackage("libde265-progs")
def _(self):
    return self.default_progs()
