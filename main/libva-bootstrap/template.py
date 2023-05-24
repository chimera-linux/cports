pkgname = "libva-bootstrap"
pkgver = "2.18.0"
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
sha256 = "9d666c70c12dfefcdd27ae7dea771557f75e24961d0ed4cb050d96fb6136f438"
options = ["!lto", "!scanshlibs", "!scanpkgconf"]


def post_install(self):
    self.install_license("COPYING")
