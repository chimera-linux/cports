pkgname = "corectrl"
pkgver = "1.5.2"
pkgrel = 0
build_style = "cmake"
# needs https://github.com/rollbear/trompeloeil
configure_args = ["-DBUILD_TESTING=OFF"]
hostmakedepends = ["cmake", "ninja", "pkgconf", "qt6-qtbase", "qt6-qttools"]
makedepends = [
    "botan-devel",
    "bzip2-devel",
    "dbus-devel",
    "polkit-devel",
    "pugixml-devel",
    "qt6-qt5compat-devel",
    "qt6-qtcharts-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
    "quazip-devel",
    "spdlog-devel",
    "zlib-ng-compat-devel",
]
checkdepends = ["catch2-devel"]
depends = ["cmd:glxinfo!mesa-demos", "qt6-qtsvg"]
pkgdesc = "Hardware control application"
license = "GPL-3.0-or-later"
url = "https://gitlab.com/corectrl/corectrl"
source = f"{url}/-/archive/v{pkgver}/corectrl-v{pkgver}.tar.gz"
sha256 = "6eccc6ea82a62e8491ad516a589e12e14d52ad0aaa74166ea74f35bf1c10c38e"
# missing checkdepends
options = ["!check"]
