pkgname = "libkcompactdisc"
pkgver = "24.05.2"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DQT_MAJOR_VERSION=6"]
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://api.kde.org/libkcompactdisc/html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/libkcompactdisc-{pkgver}.tar.xz"
)
sha256 = "15bf9433f7f0b3e23698c103fd42ab9e44b23eeedc2681cfb29b72ac8add06d2"


@subpackage("libkcompactdisc-devel")
def _devel(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
