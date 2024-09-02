pkgname = "libwacom"
pkgver = "2.13.0"
pkgrel = 0
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/linuxwacom/libwacom"
source = f"{url}/releases/download/libwacom-{pkgver}/libwacom-{pkgver}.tar.xz"
sha256 = "acd18121441bbc00fc5c881fca08a33319ab814b798eac8d0be6354923f8fb08"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libwacom-devel")
def _(self):
    return self.default_devel()
