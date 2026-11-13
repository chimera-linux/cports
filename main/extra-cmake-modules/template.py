pkgname = "extra-cmake-modules"
pkgver = "6.32.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_WITH_QT6=ON"]
# expects repo git clone
make_check_args = ["-E", "KDEFetchTranslations"]
hostmakedepends = ["cmake", "ninja"]
checkdepends = ["qt6-qtdeclarative-devel", "qt6-qttools-devel"]
pkgdesc = "Extra modules and scripts for CMake"
license = "BSD-3-Clause"
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/extra-cmake-modules-{pkgver}.tar.xz"
sha256 = "305f4e2b82eb073be6ac3e50ace85578b3c0c409be262ccc51d445449e3d9312"


def post_install(self):
    self.install_license("COPYING-CMAKE-SCRIPTS")
