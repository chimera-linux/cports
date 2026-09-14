pkgname = "libde265"
pkgver = "1.1.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Open H.265 codec implementation"
license = "LGPL-3.0-or-later"
url = "http://www.libde265.org"
source = f"https://github.com/strukturag/libde265/archive/v{pkgver}.tar.gz"
sha256 = "982f7838cc25aa6bda7fd33b9b3a05621d0f9b8456dc495d5fb4977fed6dcdbc"
# no tests
options = ["!check"]


@subpackage("libde265-devel")
def _(self):
    return self.default_devel()


@subpackage("libde265-progs")
def _(self):
    return self.default_progs()
