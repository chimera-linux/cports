pkgname = "kcodecs"
pkgver = "6.20.0"
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
sha256 = "15920b9a859341b13831e6ed49baceea2e728c796fdd082128e51f8e127ff3a0"
hardening = ["vis"]


@subpackage("kcodecs-devel")
def _(self):
    return self.default_devel()
