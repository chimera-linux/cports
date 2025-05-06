pkgname = "libwacom"
pkgver = "2.15.0"
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
license = "MIT"
url = "https://github.com/linuxwacom/libwacom"
source = f"{url}/releases/download/libwacom-{pkgver}/libwacom-{pkgver}.tar.xz"
sha256 = "20cd65b1693129c3a6c003db0fe7fff7eccaf19fb04e89aaad9c20eb2151515a"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libwacom-devel")
def _(self):
    return self.default_devel()
