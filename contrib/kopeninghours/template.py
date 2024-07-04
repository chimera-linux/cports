pkgname = "kopeninghours"
pkgver = "24.05.2"
pkgrel = 0
build_style = "cmake"
# make_check_wrapper = ["wlheadless-run", "--"]
configure_args = ["-DQT_MAJOR_VERSION=6"]
hostmakedepends = [
    "bison",
    "cmake",
    "extra-cmake-modules",
    "flex",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "kholidays-devel",
    "ki18n-devel",
    "python-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE library for working with OSM opening hours"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kopeninghours/html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kopeninghours-{pkgver}.tar.xz"
)
sha256 = "648ecd8b22b4f0909674ce3a991f73167e6648b8ae35e689f816d1b0f583518c"


@subpackage("kopeninghours-devel")
def _devel(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()


@subpackage("python-kopeninghours")
def _python(self):
    self.pkgdesc = f"{pkgdesc} (python module)"
    return ["usr/lib/python*"]
