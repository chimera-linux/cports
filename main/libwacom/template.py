pkgname = "libwacom"
pkgver = "2.5.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddocumentation=disabled", "-Dtests=enabled"
]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["libgudev-devel", "libglib-devel", "libxml2-devel"]
checkdepends = ["bash"]
pkgdesc = "Library to handle Wacom tablets"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/linuxwacom/libwacom"
source = f"{url}/releases/download/{pkgname}-{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "40b69a4c38bbcbc80b1231bc115551107ebbc0ba14d2ad1c3e54355dcd876816"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libwacom-devel")
def _devel(self):
    return self.default_devel()
