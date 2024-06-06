pkgname = "libinput"
pkgver = "1.26.0"
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
source = f"https://gitlab.freedesktop.org/libinput/libinput/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "bda944e6d60741432e10f29001c3326ee8aba2968787f78611f420f90580bd8b"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libinput-devel")
def _devel(self):
    self.depends += makedepends
    return self.default_devel()
