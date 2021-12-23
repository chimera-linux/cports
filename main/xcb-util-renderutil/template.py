pkgname = "xcb-util-renderutil"
pkgver = "0.3.9"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["xcb-util-devel"]
pkgdesc = "XCB utilities library - Render extension convenience functions"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xcb.freedesktop.org"
source = f"{url}/dist/{pkgname}-{pkgver}.tar.bz2"
sha256 = "c6e97e48fb1286d6394dddb1c1732f00227c70bd1bedb7d1acabefdd340bea5b"

def post_install(self):
    self.install_license("COPYING")

@subpackage("xcb-util-renderutil-static")
def _static(self):
    return self.default_static()

@subpackage("xcb-util-renderutil-devel")
def _devel(self):
    return self.default_devel()
