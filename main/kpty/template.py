pkgname = "kpty"
pkgver = "6.27.0"
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
sha256 = "ad06bfda8df019bb2b33567ce3df539bcc107e0dfe004281e5ff9ae4617c6ecc"
hardening = ["vis"]


@subpackage("kpty-devel")
def _(self):
    return self.default_devel()
