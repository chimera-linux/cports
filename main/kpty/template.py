pkgname = "kpty"
pkgver = "6.8.0"
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
sha256 = "fbc7f390a0b8397a5163f16b140c0662c994f614a05f7e5a5161493c3cbc3e36"
hardening = ["vis"]


@subpackage("kpty-devel")
def _(self):
    return self.default_devel()
