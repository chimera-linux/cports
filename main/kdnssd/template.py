pkgname = "kdnssd"
pkgver = "6.9.0"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://api.kde.org/frameworks/kdnssd/html/index.html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kdnssd-{pkgver}.tar.xz"
sha256 = "527c5659f44097fbeb53c2bf336d2a035fbf28535f7491662c6758259e1e765a"
hardening = ["vis"]


@subpackage("kdnssd-devel")
def _(self):
    return self.default_devel()
