pkgname = "baloo-widgets"
pkgver = "26.04.2"
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
url = "https://api.kde.org/baloo-widgets/html/index.html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/baloo-widgets-{pkgver}.tar.xz"
)
sha256 = "7daf3e6821b9988c171a316cb547591fba2caca78818c2da1d409603ea93c00a"
hardening = ["vis"]


@subpackage("baloo-widgets-devel")
def _(self):
    self.depends += [
        "kio-devel",
        "qt6-qtbase-devel",
    ]
    return self.default_devel()
