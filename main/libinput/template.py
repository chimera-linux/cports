pkgname = "libinput"
pkgver = "1.26.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddocumentation=false",
    "-Dtests=true",
    "-Ddebug-gui=false",
]
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "libevdev-devel",
    "mtdev-devel",
    "udev-devel",
    "libwacom-devel",
]
checkdepends = ["check-devel", "python-pytest", "bash"]
pkgdesc = "Input abstraction library for Wayland and X"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.freedesktop.org/wiki/Software/libinput"
source = f"https://gitlab.freedesktop.org/libinput/libinput/-/archive/{pkgver}/libinput-{pkgver}.tar.gz"
sha256 = "84fdd16ba0bd3a9adf6c1ffe4292b7a644b0d70f57f81f8239fd499a801189fb"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libinput-devel")
def _devel(self):
    self.depends += makedepends
    return self.default_devel()
