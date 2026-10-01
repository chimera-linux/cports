pkgname = "libwacom"
pkgver = "2.20.0"
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
sha256 = "370b45b5e05a91960df0aeb9c9481ae05846aab92ab2d4ec66945a0da4216888"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libwacom-devel")
def _(self):
    return self.default_devel()
