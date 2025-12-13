pkgname = "libtatsu"
pkgver = "1.0.5"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "slibtool"]
makedepends = ["curl-devel", "libplist-devel"]
pkgdesc = "Interface with Apple's Tatsu Signing Server"
license = "LGPL-2.1-or-later"
url = "https://github.com/libimobiledevice/libtatsu"
source = f"{url}/releases/download/{pkgver}/libtatsu-{pkgver}.tar.bz2"
sha256 = "536fa228b14f156258e801a7f4d25a3a9dd91bb936bf6344e23171403c57e440"


@subpackage("libtatsu-devel")
def _(self):
    return self.default_devel()
