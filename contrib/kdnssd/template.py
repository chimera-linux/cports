pkgname = "kdnssd"
pkgver = "6.3.0"
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
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kdnssd-{pkgver}.tar.xz"
sha256 = "671d48d2de1a974b570eb4f5f6f6a03875fa171eade74b81396a4bb474b9712a"
# CFI: check
hardening = ["vis", "!cfi"]


@subpackage("kdnssd-devel")
def _devel(self):
    return self.default_devel()
