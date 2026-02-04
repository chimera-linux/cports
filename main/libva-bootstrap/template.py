pkgname = "libva-bootstrap"
pkgver = "2.23.0"
pkgrel = 0
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
license = "MIT"
url = "https://01.org/linuxmedia/vaapi"
source = f"https://github.com/intel/libva/archive/{pkgver}.tar.gz"
sha256 = "b10aceb30e93ddf13b2030eb70079574ba437be9b3b76065caf28a72c07e23e7"
options = ["!lto", "!scanshlibs", "!scanpkgconf", "!autosplit", "linkundefver"]


def post_install(self):
    self.install_license("COPYING")
