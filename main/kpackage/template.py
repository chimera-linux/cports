pkgname = "kpackage"
pkgver = "6.29.0"
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
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kpackage-{pkgver}.tar.xz"
sha256 = "aee3405475bfed6187abc483df6baf48e89b2b2505ee0acc1c8d37728fb9c786"
hardening = ["vis"]


@subpackage("kpackage-devel")
def _(self):
    self.depends += ["kcoreaddons-devel"]

    return self.default_devel()
