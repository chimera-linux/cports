pkgname = "libinput"
pkgver = "1.29.2"
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
sha256 = "02631a861fc6b9fb9ca6ae51cf863334e0699bf60c91c389ac420f3fa0053bdc"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libinput-devel")
def _(self):
    self.depends += makedepends
    return self.default_devel()
