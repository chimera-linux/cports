pkgname = "kpty"
pkgver = "6.29.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "extra-cmake-modules", "gettext", "ninja"]
makedepends = ["kcoreaddons-devel", "ki18n-devel", "qt6-qttools-devel"]
pkgdesc = "KDE Interface to pseudo terminal devices"
license = "LGPL-2.1-or-later"
url = "https://community.kde.org/Frameworks"
source = (
    f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kpty-{pkgver}.tar.xz"
)
sha256 = "e0ae0fe539a94cf9a01d3526c17eb74bfe1fc7a263bb780b33e0b6b005deb607"
hardening = ["vis"]


@subpackage("kpty-devel")
def _(self):
    return self.default_devel()
