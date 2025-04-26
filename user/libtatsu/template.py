pkgname = "libtatsu"
pkgver = "1.0.4"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "slibtool"]
makedepends = ["curl-devel", "libplist-devel"]
pkgdesc = "Tatsu Signing Server communication library"
license = "LGPL-2.1-or-later"
url = "https://github.com/libimobiledevice/libtatsu"
source = f"{url}/releases/download/{pkgver}/libtatsu-{pkgver}.tar.bz2"
sha256 = "08094e58364858360e1743648581d9bad055ba3b06e398c660e481ebe0ae20b3"


@subpackage("libtatsu-devel")
def _(self):
    return self.default_devel()
