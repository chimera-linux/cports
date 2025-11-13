pkgname = "libkcompactdisc"
pkgver = "25.08.3"
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
sha256 = "3d7a9e8ab4dc149708ba459bee0ba65be854eaec78c97f7ba7f8f6632ae38670"


@subpackage("libkcompactdisc-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
