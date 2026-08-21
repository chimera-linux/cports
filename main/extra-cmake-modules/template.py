pkgname = "extra-cmake-modules"
pkgver = "6.29.0"
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
sha256 = "aaf2542edd5c5af9ea56a46468892d38a7978af65f0f3518379fa8ce66cad2b8"


def post_install(self):
    self.install_license("COPYING-CMAKE-SCRIPTS")
