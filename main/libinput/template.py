pkgname = "libinput"
pkgver = "1.28.1"
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
    "libwacom-devel",
    "mtdev-devel",
    "udev-devel",
]
checkdepends = ["check-devel", "python-pytest", "bash"]
pkgdesc = "Input abstraction library for Wayland and X"
license = "MIT"
url = "https://www.freedesktop.org/wiki/Software/libinput"
source = f"https://gitlab.freedesktop.org/libinput/libinput/-/archive/{pkgver}/libinput-{pkgver}.tar.gz"
sha256 = "a13f8c9a7d93df3c85c66afd135f0296701d8d32f911991b7aa4273fdd6a42a3"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libinput-devel")
def _(self):
    self.depends += makedepends
    return self.default_devel()
