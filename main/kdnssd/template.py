pkgname = "kdnssd"
pkgver = "6.20.0"
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
sha256 = "fc616e7f9d56ff4304a5bdc6d04e7ef75e5ff7d84375175f0b25a44ba89af60a"
hardening = ["vis"]


@subpackage("kdnssd-devel")
def _(self):
    return self.default_devel()
