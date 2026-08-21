pkgname = "solid"
pkgver = "6.29.0"
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
sha256 = "1f46e8a508cc39ae20736861b2d19a73148333f2e23495c115aa2680538a86c2"
hardening = ["vis"]


@subpackage("solid-devel")
def _(self):
    return self.default_devel()
