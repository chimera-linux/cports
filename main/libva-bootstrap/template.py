pkgname = "libva-bootstrap"
pkgver = "2.24.1"
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
sha256 = "0b4a3649ee8d683b9cce2ef094df4fb039d276c0cef7e49337c43d3b297b9f42"
options = ["!lto", "!scanshlibs", "!scanpkgconf", "!autosplit", "linkundefver"]


def post_install(self):
    self.install_license("COPYING")
