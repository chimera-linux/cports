pkgname = "libva"
pkgver = "2.20.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dwith_glx=yes", "-Dwith_wayland=yes"]
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = [
    "libxfixes-devel",
    "libxext-devel",
    "libdrm-devel",
    "libffi-devel",
    "wayland-devel",
    "mesa-devel",
]
pkgdesc = "Video Acceleration API"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://01.org/linuxmedia/vaapi"
source = f"https://github.com/intel/libva/archive/{pkgver}.tar.gz"
sha256 = "117f8d658a5fc9ea406ca80a3eb4ae1d70b15a54807c9ed77199c812bed73b60"
options = ["linkundefver"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libva-devel")
def _devel(self):
    return self.default_devel()
