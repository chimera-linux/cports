pkgname = "kpty"
pkgver = "6.30.0"
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
sha256 = "ad66149c20470de29d483f0ccdcb057d42ccf778f3f8cc8e68aefca5380bace7"
hardening = ["vis"]


@subpackage("kpty-devel")
def _(self):
    return self.default_devel()
