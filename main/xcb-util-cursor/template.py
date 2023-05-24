pkgname = "xcb-util-cursor"
pkgver = "0.1.4"
pkgrel = 0
build_style = "gnu_configure"
configure_env = {"M4": "/usr/bin/gm4"}
hostmakedepends = ["pkgconf", "gm4"]
makedepends = ["xcb-util-renderutil-devel", "xcb-util-image-devel"]
pkgdesc = "XCB utilities library - port of libxcursor"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT"
url = "https://xcb.freedesktop.org"
source = f"{url}/dist/{pkgname}-{pkgver}.tar.gz"
sha256 = "cc8608ebb695742b6cf84712be29b2b66aa5f6768039528794fca0fa283022bf"


def post_install(self):
    self.install_license("COPYING")


@subpackage("xcb-util-cursor-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
