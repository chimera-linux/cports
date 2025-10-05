pkgname = "kcodecs"
pkgver = "6.18.0"
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
sha256 = "247eda9ade502699062c7baaca7bb93691a308f202c165954652875ebe777426"
hardening = ["vis"]


@subpackage("kcodecs-devel")
def _(self):
    return self.default_devel()
