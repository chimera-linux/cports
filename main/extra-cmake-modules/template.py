pkgname = "extra-cmake-modules"
pkgver = "6.11.0"
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
sha256 = "69fdab5f0fedfb73d1accff5012d510b486e1dd75c711e925a6912a3e71814b0"


def post_install(self):
    self.install_license("COPYING-CMAKE-SCRIPTS")
