pkgname = "kpty"
pkgver = "6.31.0"
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
sha256 = "432b0a8fed2d355e19131e3f63c7856e5cb26fe4932ecb840be9465fa072bcea"
hardening = ["vis"]


@subpackage("kpty-devel")
def _(self):
    return self.default_devel()
