pkgname = "libwacom"
pkgver = "2.7.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddocumentation=disabled", "-Dtests=enabled"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["libgudev-devel", "glib-devel", "libxml2-devel"]
checkdepends = ["bash"]
pkgdesc = "Library to handle Wacom tablets"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/linuxwacom/libwacom"
source = f"{url}/releases/download/{pkgname}-{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "853929bd73fba2064b12142dbbee4b3bf84509197ff46a4da559eddf62d32cdf"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libwacom-devel")
def _devel(self):
    return self.default_devel()
