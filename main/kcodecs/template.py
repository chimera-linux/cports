pkgname = "kcodecs"
pkgver = "6.28.0"
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
url = "https://api.kde.org/frameworks/kcodecs/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kcodecs-{pkgver}.tar.xz"
sha256 = "b0a9ae34b389c6460adad5323d21bb9e43638acb58da9685f8dc8d821c38a4d8"
hardening = ["vis"]


@subpackage("kcodecs-devel")
def _(self):
    return self.default_devel()
