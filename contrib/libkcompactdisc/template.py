pkgname = "libkcompactdisc"
pkgver = "24.05.1"
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
sha256 = "10340f3c63b4d76702b5cc7ec2b36adc2ae75bffe1dd21d24a435f421a464e1c"


@subpackage("libkcompactdisc-devel")
def _devel(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
