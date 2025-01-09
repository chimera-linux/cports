pkgname = "solid"
pkgver = "6.9.1"
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
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/solid-{pkgver}.tar.xz"
sha256 = "254d562da6611a15f1f617e7afb78d4702455b89ca95de1dba9f6b9928320367"
hardening = ["vis"]


@subpackage("solid-devel")
def _(self):
    return self.default_devel()
