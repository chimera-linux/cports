pkgname = "kpty"
pkgver = "6.11.0"
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
    f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kpty-{pkgver}.tar.xz"
)
sha256 = "f1d985bf0a14061a764c7c01bcb6cf284a59ad82de13e72cfd1bd268819eebc2"
hardening = ["vis"]


@subpackage("kpty-devel")
def _(self):
    return self.default_devel()
