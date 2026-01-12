pkgname = "kpty"
pkgver = "6.22.0"
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
sha256 = "e974ae36e609d1fb485782139f8c6aa260fcee8f651da3dd0d175dad1c0b9663"
hardening = ["vis"]


@subpackage("kpty-devel")
def _(self):
    return self.default_devel()
