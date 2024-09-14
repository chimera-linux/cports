pkgname = "kcodecs"
pkgver = "6.6.0"
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
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kcodecs-{pkgver}.tar.xz"
sha256 = "d9dc2e3294aa32684990bde01bb88dedb2610a28d7c1d62a178a393fa566123b"
hardening = ["vis"]


@subpackage("kcodecs-devel")
def _(self):
    return self.default_devel()
