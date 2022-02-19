pkgname = "xcb-util-xrm"
pkgver = "1.3"
pkgrel = 0
build_style = "gnu_configure"
configure_env = {"M4": "/usr/bin/gm4"}
hostmakedepends = ["pkgconf", "xorg-util-macros", "gm4"]
makedepends = ["libx11-devel", "xcb-util-devel", "musl-bsd-headers"]
pkgdesc = "XCB utilities library - X resource manager"
maintainer = "Wesley Moore <wes@wezm.net>"
license = "MIT"
url = "https://github.com/Airblader/xcb-util-xrm"
source = f"{url}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "0129f74c327ae65e2f4ad4002f300b4f02c9aff78c00997f1f1c5a430f922f34"

def post_install(self):
    self.install_license("COPYING")

@subpackage("xcb-util-xrm-devel")
def _devel(self):
    return self.default_devel()
