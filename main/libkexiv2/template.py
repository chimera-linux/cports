pkgname = "libkexiv2"
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
    "exiv2-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "KDE wrapper around exiv2"
license = "GPL-2.0-or-later"
url = "https://api.kde.org/libkexiv2/html/index.html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/libkexiv2-{pkgver}.tar.xz"
sha256 = "f0669527d1fe7ef22c3ef7c8270ef29deafb0923ec782a22f1ced1b775367190"
hardening = ["vis"]


@subpackage("libkexiv2-devel")
def _(self):
    return self.default_devel()
