pkgname = "kpty"
pkgver = "6.16.0"
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
sha256 = "9761b1f5af7fa10e7e3ca8b52a9a10e24af994de7ae642c155dba7c99b14e9cf"
hardening = ["vis"]


@subpackage("kpty-devel")
def _(self):
    return self.default_devel()
