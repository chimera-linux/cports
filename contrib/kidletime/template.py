pkgname = "kidletime"
pkgver = "6.3.0"
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
sha256 = "cd8f677cce6738342b88817d0e7c1803460f00e409d730c5ae0ea33b1426472d"
# FIXME: cfi breaks at least 50+ kwin tests (together with kglobalacceld)
hardening = ["vis", "!cfi"]


@subpackage("kidletime-devel")
def _devel(self):
    return self.default_devel()
