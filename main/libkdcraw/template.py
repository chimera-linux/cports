pkgname = "libkdcraw"
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
    "libraw-devel",
    "qt6-qtbase-devel",
]
pkgdesc = "KDE wrapper around libraw"
license = "GPL-2.0-or-later"
url = "https://api.kde.org/libkdcraw/html/index.html"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/libkdcraw-{pkgver}.tar.xz"
sha256 = "f3f397fbecc63f0a6ed5ec2c3470b0a8754963376b9c7125a3e9f52b6768e32e"
hardening = ["vis"]


@subpackage("libkdcraw-devel")
def _(self):
    return self.default_devel()
