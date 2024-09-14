pkgname = "solid"
pkgver = "6.6.0"
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
sha256 = "88f67f369c720aaa0d347ee09273684335505c4f8faf5f7684d1acb7229455f1"
hardening = ["vis"]


@subpackage("solid-devel")
def _(self):
    return self.default_devel()
