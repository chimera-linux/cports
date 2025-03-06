pkgname = "libwacom"
pkgver = "2.14.0"
pkgrel = 1
build_style = "meson"
configure_args = ["-Ddocumentation=disabled", "-Dtests=enabled"]
make_check_args = ["--timeout-multiplier", "4"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "glib-devel",
    "libevdev-devel",
    "libgudev-devel",
    "libxml2-devel",
]
depends = ["python-libevdev", "python-pyudev"]
checkdepends = ["bash", "python-pytest", *depends]
pkgdesc = "Library to handle Wacom tablets"
license = "MIT"
url = "https://github.com/linuxwacom/libwacom"
source = f"{url}/releases/download/libwacom-{pkgver}/libwacom-{pkgver}.tar.xz"
sha256 = "5900b3ad3d780e1b864103ace99cace9470db727a162517e1648c86a1bdec0e3"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libwacom-devel")
def _(self):
    return self.default_devel()
