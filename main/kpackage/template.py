pkgname = "kpackage"
pkgver = "6.17.0"
pkgrel = 0
build_style = "cmake"
# flaky createAndUpdatePackage() Could not delete package from: /tmp/.qttest/share/packageRoot/plasmoid_to_package/
make_check_args = ["-E", "plasmoidpackagetest"]
hostmakedepends = ["cmake", "extra-cmake-modules", "gettext", "ninja"]
makedepends = [
    "karchive-devel",
    "kcoreaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE Installation and loading of additional content as packages"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kpackage/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kpackage-{pkgver}.tar.xz"
sha256 = "78d231a223394922d02957e17917a208de0e98224f21fc10e538ac971bdb42a4"
hardening = ["vis"]


@subpackage("kpackage-devel")
def _(self):
    self.depends += ["kcoreaddons-devel"]

    return self.default_devel()
