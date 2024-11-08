pkgname = "solid"
pkgver = "6.8.0"
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
sha256 = "ace5145f59db548bcf423cb6b70fd870fefba37f07a649164394a802b3ca7941"
hardening = ["vis"]


@subpackage("solid-devel")
def _(self):
    return self.default_devel()
