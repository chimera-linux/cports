pkgname = "kdnssd"
pkgver = "6.2.0"
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
sha256 = "509011367c11c3b17034d743ea6934951a6fc525b9527d18c38af81f60b08f45"
# CFI: check
hardening = ["vis", "!cfi"]


@subpackage("kdnssd-devel")
def _devel(self):
    return self.default_devel()
