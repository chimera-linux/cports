pkgname = "libwacom"
pkgver = "2.4.0"
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
sha256 = "d0d022761e3f9ab23e329583b7d2bd470b0450dfb077caeb22c5a0d66c2bd414"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libwacom-devel")
def _devel(self):
    return self.default_devel()
