pkgname = "extra-cmake-modules"
pkgver = "6.18.0"
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
sha256 = "b2d2222cfe5ace502c60bd8a77a79bc0230f48cee83265c89dcc2618b960e293"


def post_install(self):
    self.install_license("COPYING-CMAKE-SCRIPTS")
