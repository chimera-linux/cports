pkgname = "kpty"
pkgver = "6.5.0"
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
sha256 = "dc9365ba4a83b948a8326f2f75d46d4dea8327bc06b5ee2190306cbf8fdf5241"
hardening = ["vis"]


@subpackage("kpty-devel")
def _devel(self):
    return self.default_devel()
