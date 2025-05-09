pkgname = "libkdcraw"
pkgver = "25.04.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    # manual test bins
    "-DBUILD_TESTING=OFF",
    "-DQT_MAJOR_VERSION=6",
]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "libraw-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "KDE wrapper around libraw"
license = "GPL-2.0-or-later"
url = "https://api.kde.org/libkdcraw/html/index.html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/libkdcraw-{pkgver}.tar.xz"
sha256 = "6cc5f741778a7e27b6b9ab2b0c17d8145f3d197a22452f608eed7616cd6b26d6"
hardening = ["vis"]


@subpackage("libkdcraw-devel")
def _(self):
    return self.default_devel()
