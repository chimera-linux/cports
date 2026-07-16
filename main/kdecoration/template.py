pkgname = "kdecoration"
pkgver = "6.7.3"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "ki18n-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "KDE Plugin based library to create window decorations"
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://api.kde.org/plasma/kdecoration/html"
source = f"$(KDE_SITE)/plasma/{pkgver}/kdecoration-{pkgver}.tar.xz"
sha256 = "69690713d2216323dae96d61d74e087bd9e5e5b3effcf1c54f7a3e823672d0e7"
hardening = ["vis"]


@subpackage("kdecoration-devel")
def _(self):
    return self.default_devel()
