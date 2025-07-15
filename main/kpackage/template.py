pkgname = "kpackage"
pkgver = "6.16.0"
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
sha256 = "a45fce1026db3b65cdd1dd0e11374808e2686914a062f6644ebaa8ed308ee3cb"
hardening = ["vis"]


@subpackage("kpackage-devel")
def _(self):
    self.depends += ["kcoreaddons-devel"]

    return self.default_devel()
