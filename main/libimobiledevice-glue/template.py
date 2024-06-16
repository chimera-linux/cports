pkgname = "libimobiledevice-glue"
pkgver = "1.3.0"
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
sha256 = "96ec4eb2b1e217392149eafb2b5c3cd3e7110200f0e2bb5003c37d3ead7244ef"


@subpackage("libimobiledevice-glue-devel")
def _devel(self):
    return self.default_devel()
