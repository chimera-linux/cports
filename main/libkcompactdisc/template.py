pkgname = "libkcompactdisc"
pkgver = "25.04.3"
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
sha256 = "ee0be866b6f941cdf6b3c87a45861bc7685a5ba9875caf8e5f46841d8322d37f"


@subpackage("libkcompactdisc-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
