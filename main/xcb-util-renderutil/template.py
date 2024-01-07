pkgname = "xcb-util-renderutil"
pkgver = "0.3.10"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["xcb-util-devel"]
pkgdesc = "XCB utilities library - Render extension convenience functions"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xcb.freedesktop.org"
source = f"{url}/dist/{pkgname}-{pkgver}.tar.gz"
sha256 = "e04143c48e1644c5e074243fa293d88f99005b3c50d1d54358954404e635128a"


def post_install(self):
    self.install_license("COPYING")


@subpackage("xcb-util-renderutil-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
