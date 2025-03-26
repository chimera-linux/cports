pkgname = "libinput"
pkgver = "1.28.0"
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
license = "MIT"
url = "https://www.freedesktop.org/wiki/Software/libinput"
source = f"https://gitlab.freedesktop.org/libinput/libinput/-/archive/{pkgver}/libinput-{pkgver}.tar.gz"
sha256 = "d4719ff614835b305f9649899c5c2966f47e9295fa1b3925787d00171f869c21"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libinput-devel")
def _(self):
    self.depends += makedepends
    return self.default_devel()
