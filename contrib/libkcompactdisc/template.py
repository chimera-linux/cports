pkgname = "libkcompactdisc"
pkgver = "24.08.1"
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
sha256 = "45624b7252fcbe30f6e105ff8bcf8e844cb56c1cd3de26425c1bdac1e7c92eb6"


@subpackage("libkcompactdisc-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
