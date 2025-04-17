pkgname = "libkexiv2"
pkgver = "25.04.0"
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
sha256 = "1381a5ddbb421c51c5f9f72df8f33ba8b649c3627fa9f3002c1d0d2b60c94879"
hardening = ["vis"]


@subpackage("libkexiv2-devel")
def _(self):
    return self.default_devel()
