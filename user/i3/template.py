pkgname = "i3"
pkgver = "4.24"
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
sha256 = "5baefd0e5e78f1bafb7ac85deea42bcd3cbfe65f1279aa96f7e49661637ac981"
# Check phase depends on X11::XCB perl module, which isn't packaged
# Debian disables tests as well for what it's worth
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
