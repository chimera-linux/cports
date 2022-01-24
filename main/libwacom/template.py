pkgname = "libwacom"
pkgver = "2.0.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    # tests TODO: need python-libevdev, python-pyudev
    "-Ddocumentation=disabled", "-Dtests=disabled"
]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["libgudev-devel", "libglib-devel", "libxml2-devel"]
checkdepends = ["bash"]
pkgdesc = "Library to handle Wacom tablets"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/linuxwacom/libwacom"
source = f"https://github.com/linuxwacom/{pkgname}/releases/download/{pkgname}-{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "4923bdf3e7b4940bd81d3e7c1b8ab1843597a1bdf1e6f627840e0c87c381fe0a"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libwacom-devel")
def _devel(self):
    return self.default_devel()
