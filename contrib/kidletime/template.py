pkgname = "kidletime"
pkgver = "6.2.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "libxscrnsaver-devel",
    "plasma-wayland-protocols",
    "qt6-qtbase-devel",
    "qt6-qtwayland-devel",
    "wayland-protocols",
]
pkgdesc = "KDE Idle time reporting of user and system"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-only"
url = "https://api.kde.org/frameworks/kidletime/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kidletime-{pkgver}.tar.xz"
sha256 = "069182e4abfb83f93661d5bb0eaeb14b44e3705fa3492dbdb8ec03bfe6e3d9dc"
# FIXME: cfi breaks at least 50+ kwin tests (together with kglobalacceld)
hardening = ["vis", "!cfi"]


@subpackage("kidletime-devel")
def _devel(self):
    return self.default_devel()
