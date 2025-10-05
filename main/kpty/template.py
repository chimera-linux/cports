pkgname = "kpty"
pkgver = "6.18.0"
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
sha256 = "3f800638fcc0dbea0810930a1f2decfa6b894bb00732ff8646182c7dfd2ac76d"
hardening = ["vis"]


@subpackage("kpty-devel")
def _(self):
    return self.default_devel()
