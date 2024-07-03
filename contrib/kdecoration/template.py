pkgname = "kdecoration"
pkgver = "6.1.2"
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
sha256 = "81e85dd278bcfee3c90f1b5f908ee85f289eee6afad1d64964f990f9c6edbebe"
# FIXME: cfi breaks at least 20+ kwin tests
hardening = ["vis", "!cfi"]


@subpackage("kdecoration-devel")
def _devel(self):
    return self.default_devel()
