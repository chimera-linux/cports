pkgname = "libwacom"
pkgver = "2.11.0"
pkgrel = 1
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
sha256 = "b03f991ec82c543a42386274e1290c326934e4f25246dc3789ca3037c7181344"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libwacom-devel")
def _devel(self):
    return self.default_devel()
