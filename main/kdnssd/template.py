pkgname = "kdnssd"
pkgver = "6.19.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "avahi-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE zeroconf integration"
license = "GPL-2.0-or-later"
url = "https://api.kde.org/frameworks/kdnssd/html/index.html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kdnssd-{pkgver}.tar.xz"
sha256 = "9a4e9e653c6670b4681516ceade3d2664d577f5e6f0173d7bb9bbe5dd009c271"
hardening = ["vis"]


@subpackage("kdnssd-devel")
def _(self):
    return self.default_devel()
