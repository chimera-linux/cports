pkgname = "libimobiledevice-glue"
pkgver = "1.2.0"
pkgrel = 1
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
sha256 = "ff9cbc240c9780edfa43914a057b86362054053721b65fb04f54a25023b92b62"


@subpackage("libimobiledevice-glue-devel")
def _devel(self):
    return self.default_devel()
