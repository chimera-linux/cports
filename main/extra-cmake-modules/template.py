pkgname = "extra-cmake-modules"
pkgver = "6.31.0"
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
sha256 = "8f74af329e4c918358bfe54316f8cf4d530c28444595a3e2fb15075f72877f17"


def post_install(self):
    self.install_license("COPYING-CMAKE-SCRIPTS")
