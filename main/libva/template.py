pkgname = "libva"
pkgver = "2.21.0"
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
sha256 = "f7c3fffef3f04eb146e036dad2587d852bfb70e4926d014bf437244915ef7425"
options = ["linkundefver"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libva-devel")
def _devel(self):
    return self.default_devel()
