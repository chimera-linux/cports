pkgname = "kpty"
pkgver = "6.6.0"
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
sha256 = "63a1deb95284c8ff2fb77404a81183dd77d96458d05110b468742b3a0f755e61"
hardening = ["vis"]


@subpackage("kpty-devel")
def _(self):
    return self.default_devel()
