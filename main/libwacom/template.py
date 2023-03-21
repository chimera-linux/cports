pkgname = "libwacom"
pkgver = "2.6.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddocumentation=disabled", "-Dtests=enabled"
]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["libgudev-devel", "glib-devel", "libxml2-devel"]
checkdepends = ["bash"]
pkgdesc = "Library to handle Wacom tablets"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/linuxwacom/libwacom"
source = f"{url}/releases/download/{pkgname}-{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "2376cca99475235b75053a2cfbc7ed40fd8763d5a516941a664870ff1f3aa98f"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libwacom-devel")
def _devel(self):
    return self.default_devel()
