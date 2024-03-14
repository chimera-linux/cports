pkgname = "libva-bootstrap"
pkgver = "2.21.0"
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
sha256 = "f7c3fffef3f04eb146e036dad2587d852bfb70e4926d014bf437244915ef7425"
options = ["!lto", "!scanshlibs", "!scanpkgconf", "!autosplit", "linkundefver"]


def post_install(self):
    self.install_license("COPYING")
