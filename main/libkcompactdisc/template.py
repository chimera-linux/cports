pkgname = "libkcompactdisc"
pkgver = "25.12.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "ki18n-devel",
    "phonon-devel",
    "qt6-qtbase-devel",
    "solid-devel",
]
pkgdesc = "KDE library for interfacing with CDs"
license = "GPL-2.0-or-later"
url = "https://api.kde.org/libkcompactdisc/html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/libkcompactdisc-{pkgver}.tar.xz"
)
sha256 = "02e5bb5330a2dd9fbae0dba1e1c8536a78dc1f88ba2756e8b96f928156d3c180"


@subpackage("libkcompactdisc-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
