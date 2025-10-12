pkgname = "karchive"
pkgver = "6.19.0"
pkgrel = 0
build_style = "cmake"
# fails with zlib-ng equality on comp data
make_check_args = ["-E", "kfiltertest"]
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
license = "LGPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://develop.kde.org/docs/features/karchive"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/karchive-{pkgver}.tar.xz"
sha256 = "944332d802d0e128cebd087ffd50b726d100347973c2037c6051c72d54512a9e"
hardening = ["vis"]


@subpackage("karchive-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
