pkgname = "libkcompactdisc"
pkgver = "25.04.2"
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
    "qt6-qtbase-devel",
    "solid-devel",
    "ki18n-devel",
    "phonon-devel",
]
pkgdesc = "KDE library for interfacing with CDs"
license = "GPL-2.0-or-later"
url = "https://api.kde.org/libkcompactdisc/html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/libkcompactdisc-{pkgver}.tar.xz"
)
sha256 = "93da92c3c6b7cd5665727674406f06beabcfeba02eb7b9445adf441ae6618d58"


@subpackage("libkcompactdisc-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
