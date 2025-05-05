pkgname = "libraw"
pkgver = "0.21.4"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "slibtool"]
makedepends = [
    "jasper-devel",
    "lcms2-devel",
    "libjpeg-turbo-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Raw image decoder library"
license = "LGPL-2.1-only OR CDDL-1.0"
url = "https://libraw.org"
source = f"{url}/data/LibRaw-{pkgver}.tar.gz"
sha256 = "6be43f19397e43214ff56aab056bf3ff4925ca14012ce5a1538a172406a09e63"


def post_install(self):
    self.install_license("COPYRIGHT")


@subpackage("libraw-devel")
def _(self):
    return self.default_devel()


@subpackage("libraw-progs")
def _(self):
    return self.default_progs()
