pkgname = "solid"
pkgver = "6.14.0"
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
sha256 = "00996f063478863fe61b902d20c96c9eb4f4ac43353e59b779b466fa62b1a8c4"
hardening = ["vis"]


@subpackage("solid-devel")
def _(self):
    return self.default_devel()
