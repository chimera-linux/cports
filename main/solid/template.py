pkgname = "solid"
pkgver = "6.22.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "bison",
    "cmake",
    "extra-cmake-modules",
    "flex",
    "ninja",
]
makedepends = [
    "libimobiledevice-devel",
    "libplist-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
    "udev-devel",
    "util-linux-mount-devel",
]
pkgdesc = "KDE Hardware integration and detection"
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://develop.kde.org/docs/features/solid"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/solid-{pkgver}.tar.xz"
sha256 = "411531542e2abc36a5c446605eaa64c62a00ef7b85148c477ba999b6109b5bf3"
hardening = ["vis"]


@subpackage("solid-devel")
def _(self):
    return self.default_devel()
