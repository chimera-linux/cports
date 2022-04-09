pkgname = "libwacom"
pkgver = "2.2.0"
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
source = f"https://github.com/linuxwacom/{pkgname}/releases/download/{pkgname}-{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "e62ac9edb522d36ad2fa99adca35ddc02067383d4668eeaa13d7efccc30bb8c8"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libwacom-devel")
def _devel(self):
    return self.default_devel()
