pkgname = "libimobiledevice-glue"
pkgver = "1.3.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = ["libplist-devel"]
pkgdesc = "Common code library for the libimobiledevice project"
license = "LGPL-2.1-or-later"
url = "https://libimobiledevice.org"
source = f"https://github.com/libimobiledevice/libimobiledevice-glue/releases/download/{pkgver}/libimobiledevice-glue-{pkgver}.tar.bz2"
sha256 = "6489a3411b874ecd81c87815d863603f518b264a976319725e0ed59935546774"


@subpackage("libimobiledevice-glue-devel")
def _(self):
    return self.default_devel()
