pkgname = "suil"
pkgver = "0.10.20"
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
sha256 = "334a3ed3e73d5e17ff400b3db9801f63809155b0faa8b1b9046f9dd3ffef934e"
hardening = ["vis", "cfi"]
# no actual tests
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("suil-devel")
def _(self):
    return self.default_devel()
