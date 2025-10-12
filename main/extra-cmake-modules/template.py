pkgname = "extra-cmake-modules"
pkgver = "6.19.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_WITH_QT6=ON"]
# expects repo git clone
make_check_args = ["-E", "KDEFetchTranslations"]
hostmakedepends = ["cmake", "ninja"]
checkdepends = ["qt6-qtdeclarative-devel", "qt6-qttools-devel"]
pkgdesc = "Extra modules and scripts for CMake"
license = "BSD-3-Clause"
url = "https://api.kde.org/frameworks/extra-cmake-modules/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/extra-cmake-modules-{pkgver}.tar.xz"
sha256 = "a4f0c1d8181f43e9af4b9b44696c77760b5bc9dae5bdb921f090bce664e9ca84"


def post_install(self):
    self.install_license("COPYING-CMAKE-SCRIPTS")
