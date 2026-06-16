pkgname = "kopeninghours"
pkgver = "26.04.2"
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
url = "https://api.kde.org/kopeninghours/html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kopeninghours-{pkgver}.tar.xz"
)
sha256 = "0001946190105da042121d93bf0102d554dd4a11bdc9b447718640698fcc63f2"


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
