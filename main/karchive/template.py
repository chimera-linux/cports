pkgname = "karchive"
pkgver = "6.32.0"
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
    "bzip2-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
pkgdesc = "Qt6 addon providing access to numerous types of archives"
license = "LGPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://develop.kde.org/docs/features/karchive"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/karchive-{pkgver}.tar.xz"
sha256 = "30687d9be0aea05a4ef887212abd91d7c4337cb9f166610f98eac2b01407fb1f"
hardening = ["vis"]


@subpackage("karchive-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
