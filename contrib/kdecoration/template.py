pkgname = "kdecoration"
pkgver = "6.1.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "ki18n-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "KDE Plugin based library to create window decorations"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://api.kde.org/plasma/kdecoration/html"
source = f"$(KDE_SITE)/plasma/{pkgver}/kdecoration-{pkgver}.tar.xz"
sha256 = "862eb19732ed1846430c4de0ef56302ac0f9aef5ad260719d2431b63dc8aafa5"
# FIXME: cfi breaks at least 20+ kwin tests
hardening = ["vis", "!cfi"]


@subpackage("kdecoration-devel")
def _devel(self):
    return self.default_devel()
