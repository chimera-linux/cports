pkgname = "kweathercore"
pkgver = "25.08.3"
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
    "kholidays-devel",
    "ki18n-devel",
    "qt6-qtbase-devel",
    "qt6-qtpositioning-devel",
]
pkgdesc = "KDE Weather library"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kweathercore/html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kweathercore-{pkgver}.tar.xz"
)
sha256 = "693573a0245bf65daceab127ac45c9acfbb39e6b7c516d817af541cd3125b25b"


@subpackage("kweathercore-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
