pkgname = "libinput"
pkgver = "1.19.1"
pkgrel = 0
build_style = "meson"
# FIXME: libwacom support?
configure_args = [
    "-Ddocumentation=false", "-Dtests=true", "-Dlibwacom=false",
    "-Ddebug-gui=false", "-Db_ndebug=false"
]
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "libevdev-devel", "mtdev-devel", "eudev-devel"
]
checkdepends = ["check-devel", "bash"]
pkgdesc = "Input abstraction library for Wayland and X"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.freedesktop.org/wiki/Software/libinput"
source = f"$(FREEDESKTOP_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "0bdcf5b1783b737854b7af1ca22df67bc36a6fe7c9cfa71f01e9149f9220446d"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libinput-devel")
def _devel(self):
    self.depends += makedepends
    return self.default_devel()
