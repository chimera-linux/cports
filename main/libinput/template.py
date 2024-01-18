pkgname = "libinput"
pkgver = "1.25.0"
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
sha256 = "f7e8425f185cadba5761d0a1dae6be041750d351163ffa04adc5b9a79a13c0ec"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libinput-devel")
def _devel(self):
    self.depends += makedepends
    return self.default_devel()
