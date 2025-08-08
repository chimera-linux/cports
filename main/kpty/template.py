pkgname = "kpty"
pkgver = "6.17.0"
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
sha256 = "96a71687a8de0becc34a8157572d2440ba8d4b976fd5d0813331dfd86b92aabb"
hardening = ["vis"]


@subpackage("kpty-devel")
def _(self):
    return self.default_devel()
