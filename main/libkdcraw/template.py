pkgname = "libkdcraw"
pkgver = "24.12.3"
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
sha256 = "982e09405cde76911f036806aa12fd6b70f8ee26b1b37c73fe5c40ddc2340d5a"
hardening = ["vis"]


@subpackage("libkdcraw-devel")
def _(self):
    return self.default_devel()
