pkgname = "kweathercore"
pkgver = "25.04.1"
pkgrel = 0
build_style = "cmake"
# needs to get location
make_check_args = ["-E", "locationquerytest"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "ki18n-devel",
    "kholidays-devel",
    "qt6-qtbase-devel",
    "qt6-qtpositioning-devel",
]
pkgdesc = "KDE Weather library"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kweathercore/html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kweathercore-{pkgver}.tar.xz"
)
sha256 = "7bf61733ffa76ac660b66f65b0e0c0ac46230d077f03cd93958d5c91a98afdf6"


@subpackage("kweathercore-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
