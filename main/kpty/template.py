pkgname = "kpty"
pkgver = "6.20.0"
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
sha256 = "6666f05f1735209da6fcae1fd21ff94ae6772d32b0a24f7b84cdb56e22202966"
hardening = ["vis"]


@subpackage("kpty-devel")
def _(self):
    return self.default_devel()
