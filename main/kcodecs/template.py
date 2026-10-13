pkgname = "kcodecs"
pkgver = "6.31.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gperf",
    "ninja",
]
makedepends = [
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
pkgdesc = "Collection of methods to manipulate strings using various encodings"
license = "LGPL-2.1-only AND LGPL-2.1-or-later"
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kcodecs-{pkgver}.tar.xz"
sha256 = "2d889f4afd881ae3bc532753c7a2758f45842d4ca828a171d52c8f396128d081"
hardening = ["vis"]


@subpackage("kcodecs-devel")
def _(self):
    return self.default_devel()
