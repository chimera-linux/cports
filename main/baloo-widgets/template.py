pkgname = "baloo-widgets"
pkgver = "25.08.0"
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
sha256 = "c77e3a761db3cfc13c96a1436bf6d733965142bad30e89001c979119bb8ebb24"
hardening = ["vis"]


@subpackage("baloo-widgets-devel")
def _(self):
    self.depends += [
        "kio-devel",
        "qt6-qtbase-devel",
    ]
    return self.default_devel()
