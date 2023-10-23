pkgname = "kdecoration"
pkgver = "6.0.5"
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
sha256 = "0a3c5161c03e8ba103fc10966abbde298de98e25c945a24ae08a539a78670224"
# FIXME: cfi breaks at least 20+ kwin tests
hardening = ["vis", "!cfi"]


@subpackage("kdecoration-devel")
def _devel(self):
    return self.default_devel()
