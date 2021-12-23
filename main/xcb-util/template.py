pkgname = "xcb-util"
pkgver = "0.4.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "gperf"]
makedepends = ["libxcb-devel"]
pkgdesc = "XCB utilities library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xcb.freedesktop.org"
source = f"{url}/dist/{pkgname}-{pkgver}.tar.bz2"
sha256 = "46e49469cb3b594af1d33176cd7565def2be3fa8be4371d62271fabb5eae50e9"

def post_install(self):
    self.install_license("COPYING")

@subpackage("xcb-util-static")
def _static(self):
    return self.default_static()

@subpackage("xcb-util-devel")
def _devel(self):
    return self.default_devel()
