pkgname = "kpty"
pkgver = "6.4.0"
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
sha256 = "68626789dcb79d9fd1b3a4c55016747260085ba4c68f7b408a5f1d190cca4623"
hardening = ["vis", "!cfi"]


@subpackage("kpty-devel")
def _devel(self):
    return self.default_devel()
