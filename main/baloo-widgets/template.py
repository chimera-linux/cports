pkgname = "baloo-widgets"
pkgver = "26.08.1"
pkgrel = 0
build_style = "cmake"
# flaky filemetadataitemcounttest when parallel
make_check_args = ["-j1"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "baloo-devel",
    "kconfig-devel",
    "ki18n-devel",
    "kio-devel",
    "kservice-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE Baloo widgets"
license = "LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only)"
url = "https://community.kde.org/Baloo"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/baloo-widgets-{pkgver}.tar.xz"
)
sha256 = "b4af5cc65d886ab9d2a807254e11295e585d7cedd993d2b3b78f2f17e3a7f544"
hardening = ["vis"]


@subpackage("baloo-widgets-devel")
def _(self):
    self.depends += [
        "kio-devel",
        "qt6-qtbase-devel",
    ]
    return self.default_devel()
