pkgname = "libimobiledevice-glue"
pkgver = "1.3.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = ["libplist-devel"]
pkgdesc = "Common code library for the libimobiledevice project"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-or-later"
url = "https://libimobiledevice.org"
source = f"https://github.com/libimobiledevice/libimobiledevice-glue/releases/download/{pkgver}/libimobiledevice-glue-{pkgver}.tar.bz2"
sha256 = "6e2849f221e6ab970566a115d42f3c20f8848e4d40c2ed61ac20dc85f40fa54f"


@subpackage("libimobiledevice-glue-devel")
def _(self):
    return self.default_devel()
