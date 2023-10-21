pkgname = "karchive"
pkgver = "6.2.0"
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
sha256 = "1435e09e64bf4cf27ceebfc76582e44db9d37b1453e55aeee09778bccfd9a8b2"
hardening = ["vis", "cfi"]


@subpackage("karchive-devel")
def _devel(self):
    return self.default_devel()
