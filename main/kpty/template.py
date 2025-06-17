pkgname = "kpty"
pkgver = "6.15.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "extra-cmake-modules", "gettext", "ninja"]
makedepends = ["kcoreaddons-devel", "ki18n-devel", "qt6-qttools-devel"]
pkgdesc = "KDE Interface to pseudo terminal devices"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kpty/html"
source = (
    f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kpty-{pkgver}.tar.xz"
)
sha256 = "d2a69c8c9cc6d696c4c717357bb6d6581f5ddf64aad83e9ae98903b1f2e0a8b1"
hardening = ["vis"]


@subpackage("kpty-devel")
def _(self):
    return self.default_devel()
