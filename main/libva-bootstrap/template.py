pkgname = "libva-bootstrap"
pkgver = "2.19.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddefault_library=shared",
    "-Dwith_glx=no",
    "-Dwith_x11=no",
    "-Dwith_wayland=no",
]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["libffi-devel", "libdrm-devel"]
depends = ["!libva", "!libva-devel"]
# no provides needed, only for mesa which needs headers
pkgdesc = "Video Acceleration API (bootstrap)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://01.org/linuxmedia/vaapi"
source = f"https://github.com/intel/libva/archive/{pkgver}.tar.gz"
sha256 = "8cb5e2a9287a76b12c0b6cb96f4f27a0321bbe693df43cd950e5d4542db7f227"
options = ["!lto", "!scanshlibs", "!scanpkgconf"]


def post_install(self):
    self.install_license("COPYING")
