pkgname = "karchive"
pkgver = "6.3.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
    "zstd-devel",
]
pkgdesc = "Qt6 addon providing access to numerous types of archives"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://develop.kde.org/docs/features/karchive"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/karchive-{pkgver}.tar.xz"
sha256 = "27807f5707668f9aa41c898eba90198a3083577fdab9f4751a02fefe63674e29"
hardening = ["vis", "!cfi"]


@subpackage("karchive-devel")
def _devel(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
