pkgname = "solid"
pkgver = "6.32.0"
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
sha256 = "9620a6065403c5097fce0518abb7d4f038f4f11327e7ce94094ae9561bce0008"
hardening = ["vis"]


@subpackage("solid-devel")
def _(self):
    return self.default_devel()
