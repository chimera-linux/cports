pkgname = "libinput"
pkgver = "1.19.3"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddocumentation=false", "-Dtests=true",
    "-Ddebug-gui=false", "-Db_ndebug=false"
]
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "libevdev-devel", "mtdev-devel", "eudev-devel", "libwacom-devel",
]
checkdepends = ["check-devel", "bash"]
pkgdesc = "Input abstraction library for Wayland and X"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.freedesktop.org/wiki/Software/libinput"
source = f"$(FREEDESKTOP_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "3cae78ccde19d7d0f387e58bc734d4d17ab5f6426f54a9e8b728c90b17baa068"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libinput-devel")
def _devel(self):
    self.depends += makedepends
    return self.default_devel()
