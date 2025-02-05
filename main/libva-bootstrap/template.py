pkgname = "libva-bootstrap"
pkgver = "2.22.0"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Ddefault_library=shared",
    "-Dwith_glx=no",
    "-Dwith_x11=no",
    "-Dwith_wayland=no",
]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["libffi8-devel", "libdrm-devel"]
depends = ["!libva", "!libva-devel"]
# no provides needed, only for mesa which needs headers
pkgdesc = "Video Acceleration API"
subdesc = "bootstrap"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://01.org/linuxmedia/vaapi"
source = f"https://github.com/intel/libva/archive/{pkgver}.tar.gz"
sha256 = "467c418c2640a178c6baad5be2e00d569842123763b80507721ab87eb7af8735"
options = ["!lto", "!scanshlibs", "!scanpkgconf", "!autosplit", "linkundefver"]


def post_install(self):
    self.install_license("COPYING")
