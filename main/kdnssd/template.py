pkgname = "kdnssd"
pkgver = "6.18.0"
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
sha256 = "c48f2881d9664c0ee12b7091c56cbb1e959a7e960cf2d52c6c87e6fcaaf13c7f"
hardening = ["vis"]


@subpackage("kdnssd-devel")
def _(self):
    return self.default_devel()
