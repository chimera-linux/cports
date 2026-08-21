pkgname = "kopeninghours"
pkgver = "26.08.0"
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
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/libraries/kopeninghours"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kopeninghours-{pkgver}.tar.xz"
)
sha256 = "b53e954f60bdebcfff1e5744b1ca62cd96065f01b25eff8f9976c75b1827862c"


@subpackage("kopeninghours-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()


@subpackage("kopeninghours-python")
def _(self):
    self.subdesc = "python module"
    # transitional
    self.provides = [self.with_pkgver("python-kopeninghours")]

    return ["usr/lib/python*"]
