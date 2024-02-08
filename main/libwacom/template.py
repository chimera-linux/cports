pkgname = "libwacom"
pkgver = "2.10.0"
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
sha256 = "3f8ef37de78ac3d08af1bdcb5d5828ec8284dcb7154bbec4995238728914aa0e"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libwacom-devel")
def _devel(self):
    return self.default_devel()
