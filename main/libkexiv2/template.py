pkgname = "libkexiv2"
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
    "exiv2-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "KDE wrapper around exiv2"
license = "GPL-2.0-or-later"
url = "https://api.kde.org/libkexiv2/html/index.html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/libkexiv2-{pkgver}.tar.xz"
sha256 = "0806898554b62a6f834d33bb481923d82bde91b1692ba7b146fec94b9a503d03"
hardening = ["vis"]


@subpackage("libkexiv2-devel")
def _(self):
    return self.default_devel()
