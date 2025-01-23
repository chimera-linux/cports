pkgname = "suil"
pkgver = "0.10.22"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dgtk2=disabled",
    "-Dgtk3=enabled",
    "-Dqt5=disabled",
]
hostmakedepends = [
    "meson",
    "ninja",
    "pkgconf",
]
makedepends = [
    "gtk+3-devel",
    "lv2",
]
pkgdesc = "C library for loading and wrapping LV2 plugin UIs"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "ISC"
url = "https://drobilla.net/software/suil.html"
source = f"https://download.drobilla.net/suil-{pkgver}.tar.xz"
sha256 = "d720969e0f44a99d5fba35c733a43ed63a16b0dab867970777efca4b25387eb7"
# no actual tests
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("suil-devel")
def _(self):
    return self.default_devel()
