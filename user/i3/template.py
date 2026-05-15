pkgname = "i3"
pkgver = "4.25.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "bash",
    "meson",
    "perl",
    "pkgconf",
]
makedepends = [
    "libev-devel",
    "libxcb-devel",
    "libxkbcommon-devel",
    "pango-devel",
    "pcre2-devel",
    "startup-notification-devel",
    "xcb-util-cursor-devel",
    "xcb-util-keysyms-devel",
    "xcb-util-wm-devel",
    "xcb-util-xrm-devel",
    "yajl-devel",
]
pkgdesc = "Dynamic tiling window manager"
license = "BSD-3-Clause"
url = "https://i3wm.org"
source = f"https://i3wm.org/downloads/i3-{pkgver}.tar.xz"
sha256 = "4a742bbe81b9e5ee6057f42a8e3c691d88894e93f1a5d81fe239128512ac05c0"
# Check phase depends on X11::XCB perl module, which isn't packaged
# Debian disables tests as well for what it's worth
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
