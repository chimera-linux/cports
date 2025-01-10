pkgname = "extra-cmake-modules"
pkgver = "6.10.0"
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
sha256 = "506989a0d400913403e669c1912238db053cd6b38dff74b17e2e6f879c79cca0"


def post_install(self):
    self.install_license("COPYING-CMAKE-SCRIPTS")
