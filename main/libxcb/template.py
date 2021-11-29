pkgname = "libxcb"
pkgver = "1.14"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-build-docs", "--enable-xinput", "--enable-xkb"]
hostmakedepends = ["pkgconf", "libtool", "xorg-util-macros", "xcbproto"]
makedepends = ["xcbproto", "libxdmcp-devel", "libxau-devel"]
pkgdesc = "X protocol C language binding"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://xcb.freedesktop.org"
source = f"{url}/dist/{pkgname}-{pkgver}.tar.xz"
sha256 = "a55ed6db98d43469801262d81dc2572ed124edc3db31059d4e9916eb9f844c34"
options = ["lto"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("libxcb-static")
def _static(self):
    return self.default_static()

@subpackage("libxcb-devel")
def _devel(self):
    self.depends += ["xcbproto"]
    return self.default_devel(extra = ["usr/share"])
