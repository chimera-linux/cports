pkgname = "libva-bootstrap"
pkgver = "2.20.0"
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
sha256 = "117f8d658a5fc9ea406ca80a3eb4ae1d70b15a54807c9ed77199c812bed73b60"
options = ["!lto", "!scanshlibs", "!scanpkgconf"]


def post_install(self):
    self.install_license("COPYING")
