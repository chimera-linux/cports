pkgname = "libinput"
pkgver = "1.29.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
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
sha256 = "ec71f6ec6632108a62756f49d86e864494108e70cf670e85f8b7579e970e152c"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libinput-devel")
def _(self):
    self.depends += makedepends
    return self.default_devel()
