pkgname = "libwacom"
pkgver = "2.9.0"
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
sha256 = "6f678156797becc4f1537a19aadcc48ed7a54e1ff3cbf591d1233f8a2d82e242"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libwacom-devel")
def _devel(self):
    return self.default_devel()
