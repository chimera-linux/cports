pkgname = "kpty"
pkgver = "6.19.0"
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
sha256 = "78544c16cecc7dbcffd0335bf945eec8103115786e1158235481ac152f4bb40c"
hardening = ["vis"]


@subpackage("kpty-devel")
def _(self):
    return self.default_devel()
