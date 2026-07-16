pkgname = "kpty"
pkgver = "6.28.0"
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
sha256 = "5a08d641e43fa8fd071d759d84e930251aa111973b362edce14d49032aa731d1"
hardening = ["vis"]


@subpackage("kpty-devel")
def _(self):
    return self.default_devel()
