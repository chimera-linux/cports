pkgname = "libkcompactdisc"
pkgver = "25.08.1"
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
sha256 = "ceb9f45732106dfff29d4f510c663b7811c32e4506e24b3bc64a0fe77cd9281c"


@subpackage("libkcompactdisc-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
