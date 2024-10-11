pkgname = "extra-cmake-modules"
pkgver = "6.7.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_WITH_QT6=ON"]
# expects repo git clone
make_check_args = ["-E", "KDEFetchTranslations"]
hostmakedepends = ["cmake", "ninja"]
checkdepends = ["qt6-qtdeclarative-devel", "qt6-qttools-devel"]
pkgdesc = "Extra modules and scripts for CMake"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "BSD-3-Clause"
url = "https://api.kde.org/frameworks/extra-cmake-modules/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/extra-cmake-modules-{pkgver}.tar.xz"
sha256 = "d81de82692d3d2bb77110332a65c8266252becc2c3f307ce814990ce5607b8dc"


def post_install(self):
    self.install_license("COPYING-CMAKE-SCRIPTS")
