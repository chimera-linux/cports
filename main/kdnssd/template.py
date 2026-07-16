pkgname = "kdnssd"
pkgver = "6.28.0"
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
sha256 = "f4fe731aad56ae010c2b42f2bd56d4499339bb0839ae2251035132f1a3708df2"
hardening = ["vis"]


@subpackage("kdnssd-devel")
def _(self):
    return self.default_devel()
