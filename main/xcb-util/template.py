pkgname = "xcb-util"
pkgver = "0.4.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "gperf"]
makedepends = ["libxcb-devel"]
pkgdesc = "XCB utilities library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xcb.freedesktop.org"
source = f"{url}/dist/{pkgname}-{pkgver}.tar.gz"
sha256 = "21c6e720162858f15fe686cef833cf96a3e2a79875f84007d76f6d00417f593a"

def post_install(self):
    self.install_license("COPYING")

@subpackage("xcb-util-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []
