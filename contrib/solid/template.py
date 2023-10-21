pkgname = "solid"
pkgver = "6.2.0"
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
    "libmount-devel",
    "libplist-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
    "udev-devel",
]
pkgdesc = "KDE Hardware integration and detection"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only OR LGPL-3.0-only"
url = "https://develop.kde.org/docs/features/solid"
source = (
    f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/solid-{pkgver}.tar.xz"
)
sha256 = "002a0d2b27599bebc721516681d327876962fdcaf9940f033634fb93a4f9d722"
hardening = ["vis", "cfi"]


@subpackage("solid-devel")
def _devel(self):
    return self.default_devel()
