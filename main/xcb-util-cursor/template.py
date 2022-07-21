pkgname = "xcb-util-cursor"
pkgver = "0.1.3"
pkgrel = 0
build_style = "gnu_configure"
configure_env = {"M4": "/usr/bin/gm4"}
hostmakedepends = ["pkgconf", "gm4"]
makedepends = ["xcb-util-renderutil-devel", "xcb-util-image-devel"]
pkgdesc = "XCB utilities library - port of libxcursor"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT"
url = "https://xcb.freedesktop.org"
source = f"{url}/dist/{pkgname}-{pkgver}.tar.bz2"
sha256 = "05a10a0706a1a789a078be297b5fb663f66a71fb7f7f1b99658264c35926394f"

def post_install(self):
    self.install_license("COPYING")

@subpackage("xcb-util-cursor-devel")
def _devel(self):
    return self.default_devel()
