pkgname = "baloo-widgets"
pkgver = "25.08.3"
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
sha256 = "fc0a8ec5321b3f4bb0e1f165cd8e7577019b90d5755170802634a68dfc3ce7cb"
hardening = ["vis"]


@subpackage("baloo-widgets-devel")
def _(self):
    self.depends += [
        "kio-devel",
        "qt6-qtbase-devel",
    ]
    return self.default_devel()
