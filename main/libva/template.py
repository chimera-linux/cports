pkgname = "libva"
pkgver = "2.13.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dwith_glx=no", "-Dwith_wayland=yes"]
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = [
    "libxfixes-devel", "libxext-devel", "libdrm-devel", "libffi-devel",
    "wayland-devel"
]
pkgdesc = "Video Acceleration API"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://01.org/linuxmedia/vaapi"
source = f"https://github.com/intel/{pkgname}/archive/{pkgver}.tar.gz"
sha256 = "6b7ec7d4fa204dad3f266450981f1f0892400c03afd3e00ac11f8ccade5aaaa1"
options = ["lto"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("libva-devel")
def _devel(self):
    return self.default_devel(man = True)
