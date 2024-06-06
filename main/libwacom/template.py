pkgname = "libwacom"
pkgver = "2.12.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddocumentation=disabled", "-Dtests=enabled"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "glib-devel",
    "libevdev-devel",
    "libgudev-devel",
    "libxml2-devel",
]
checkdepends = ["bash"]
pkgdesc = "Library to handle Wacom tablets"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/linuxwacom/libwacom"
source = f"{url}/releases/download/{pkgname}-{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "40462434a8568e3c0a75c18a5452aa50e041819363853090c4e7ba7e23a4a180"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libwacom-devel")
def _devel(self):
    return self.default_devel()
