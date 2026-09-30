pkgname = "stellarium"
pkgver = "26.3"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DENABLE_GPS=OFF",  # requires qtserialport and libgps
    "-DUSE_PLUGIN_TELESCOPECONTROL=OFF",  # requires qtserialport and indi
    "-DENABLE_TESTING=ON",
]
hostmakedepends = [
    "cmake",
    "doxygen",
    "gettext",
    "graphviz",
    "ninja",
    "perl",
]
makedepends = [
    "calcmysky-devel",
    "exiv2-devel",
    "md4c-devel",
    "nlopt-devel",
    "qt6-qtbase-devel",
    "qt6-qtcharts-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qtpositioning-devel",
    "qt6-qtspeech-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
    "qt6-qtwebengine-devel",
    "qxlsx-devel",
    "zlib-ng-compat-devel",
]
depends = [
    # dlopened
    "so:libShowMySky-Qt6.so.15!calcmysky",
]
pkgdesc = "Desktop planetarium"
license = "GPL-2.0-or-later"
url = "https://stellarium.org"
source = f"https://github.com/Stellarium/stellarium/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "979716e89df588eb0a7df33c414c22c0d3c0ead0a455bdfe87ae827cafd8e254"


@subpackage("stellarium-locale")
def _(self):
    self.subdesc = "locale data"
    self.install_if = ["base-locale", self.parent]
    # one level deeper than usual
    return ["usr/share/stellarium/translations/*/*.qm"]
