pkgname = "suil"
pkgver = "0.10.18"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "ISC"
url = "https://drobilla.net/software/suil.html"
source = f"https://download.drobilla.net/suil-{pkgver}.tar.xz"
sha256 = "84ada094fbe17ad3e765379002f3a0c7149b43b020235e4d7fa41432f206f85f"
hardening = ["vis", "cfi"]
# no actual tests
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("suil-devel")
def _devel(self):
    return self.default_devel()
