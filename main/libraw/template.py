pkgname = "libraw"
pkgver = "0.21.3"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-only OR CDDL-1.0"
url = "https://libraw.org"
source = f"{url}/data/LibRaw-{pkgver}.tar.gz"
sha256 = "dba34b7fc1143503942fa32ad9db43e94f714e62a4a856e91617f8f3e1e0aa5c"


def post_install(self):
    self.install_license("COPYRIGHT")


@subpackage("libraw-devel")
def _(self):
    return self.default_devel()


@subpackage("libraw-progs")
def _(self):
    return self.default_progs()
