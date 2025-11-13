pkgname = "libkdcraw"
pkgver = "25.08.3"
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
sha256 = "52fa78d013e13c72c62fb4d6868ef10a8c11d89948a6d24415647e917aa72cdf"
hardening = ["vis"]


@subpackage("libkdcraw-devel")
def _(self):
    return self.default_devel()
