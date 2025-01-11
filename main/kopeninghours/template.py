pkgname = "kopeninghours"
pkgver = "24.12.1"
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
sha256 = "668681ed05df9d038533e291cd759d1b4583b82baa65291628d4b77fc885127d"


@subpackage("kopeninghours-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()


@subpackage("python-kopeninghours")
def _(self):
    self.subdesc = "python module"
    return ["usr/lib/python*"]
