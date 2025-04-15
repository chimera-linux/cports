pkgname = "kpty"
pkgver = "6.13.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "kcoreaddons-devel",
    "ki18n-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "KDE Interface to pseudo terminal devices"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kpty/html"
source = (
    f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kpty-{pkgver}.tar.xz"
)
sha256 = "afa8fa8c579bd2ca4b0cccc69427f9035fa7d76cefe258639ec17d966aa43513"
hardening = ["vis"]


@subpackage("kpty-devel")
def _(self):
    return self.default_devel()
