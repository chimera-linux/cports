pkgname = "ayatana-ido"
pkgver = "0.10.2"
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
sha256 = "0daf8a2e5bba51225bc3724c0e53c3b569269f28ac3a14f6bed9920b44ecc856"
options = ["!cross"]


@subpackage("ayatana-ido-devel")
def _devel(self):
    return self.default_devel()
