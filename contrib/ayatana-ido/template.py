pkgname = "ayatana-ido"
pkgver = "0.10.4"
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
sha256 = "bd59abd5f1314e411d0d55ce3643e91cef633271f58126be529de5fb71c5ab38"
options = ["!cross"]


@subpackage("ayatana-ido-devel")
def _(self):
    return self.default_devel()
