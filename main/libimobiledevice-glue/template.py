pkgname = "libimobiledevice-glue"
pkgver = "1.3.3"
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
sha256 = "920ce01382a32695f49b23292b4979a03f0afd16c58e8755d8b7f41804acc1a9"


@subpackage("libimobiledevice-glue-devel")
def _(self):
    return self.default_devel()
