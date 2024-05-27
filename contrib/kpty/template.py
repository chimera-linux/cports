pkgname = "kpty"
pkgver = "6.2.0"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kpty/html"
source = (
    f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kpty-{pkgver}.tar.xz"
)
sha256 = "f7683e8b5cd5dbbd4257e8d5acd26e58685a3bc3f161dc0fe10f53a075240264"
hardening = ["vis", "cfi"]


@subpackage("kpty-devel")
def _devel(self):
    return self.default_devel()
