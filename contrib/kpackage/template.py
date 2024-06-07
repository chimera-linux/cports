pkgname = "kpackage"
pkgver = "6.3.0"
pkgrel = 0
build_style = "cmake"
# flaky createAndUpdatePackage() Could not delete package from: /tmp/.qttest/share/packageRoot/plasmoid_to_package/
make_check_args = ["-E", "plasmoidpackagetest"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "karchive-devel",
    "kcoreaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "KDE Installation and loading of additional content as packages"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kpackage/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kpackage-{pkgver}.tar.xz"
sha256 = "811d6809e091c1eaaa07cafeacc86eb23fa55ed038f8f1a93d259e5734510b4d"
hardening = ["vis", "!cfi"]


@subpackage("kpackage-devel")
def _devel(self):
    self.depends += ["kcoreaddons-devel"]

    return self.default_devel()
