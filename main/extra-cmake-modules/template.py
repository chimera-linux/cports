pkgname = "extra-cmake-modules"
pkgver = "6.9.0"
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
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/extra-cmake-modules-{pkgver}.tar.xz"
sha256 = "cec06b25e166edb71a1a973641c4f5fc3c8712dde3fb3e639db586515cc1642e"


def post_install(self):
    self.install_license("COPYING-CMAKE-SCRIPTS")
