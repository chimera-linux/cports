pkgname = "ayatana-ido"
pkgver = "0.10.3"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DENABLE_TESTS=ON"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "glib-devel",
    "gobject-introspection",
    "ninja",
    "pkgconf",
    "vala",
]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
]
checkdepends = ["gtest-devel", "xwayland-run"]
pkgdesc = "Ayatana Indicator Display Objects"
maintainer = "triallax <triallax@tutanota.com>"
license = (
    "GPL-3.0-only AND LGPL-2.1-or-later AND (LGPL-2.1-only OR LGPL-3.0-only)"
)
url = "https://github.com/AyatanaIndicators/ayatana-ido"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "45580033e9b52185c41ce500c68281ae724e7e5a553425685c0b89ffcd9cda66"
options = ["!cross"]


@subpackage("ayatana-ido-devel")
def _(self):
    return self.default_devel()
