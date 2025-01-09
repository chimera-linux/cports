pkgname = "kcodecs"
pkgver = "6.9.0"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only AND LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kcodecs/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kcodecs-{pkgver}.tar.xz"
sha256 = "c88a4def4564a746bb8a6a7c127094ae9b7e47e1a5ad24f87ffb6643d42b0cb1"
hardening = ["vis"]


@subpackage("kcodecs-devel")
def _(self):
    return self.default_devel()
