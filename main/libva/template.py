pkgname = "libva"
pkgver = "2.22.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dwith_glx=yes", "-Dwith_wayland=yes"]
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = [
    "libdrm-devel",
    "libffi8-devel",
    "libxext-devel",
    "libxfixes-devel",
    "mesa-devel",
    "wayland-devel",
]
pkgdesc = "Video Acceleration API"
license = "MIT"
url = "https://01.org/linuxmedia/vaapi"
source = f"https://github.com/intel/libva/archive/{pkgver}.tar.gz"
sha256 = "467c418c2640a178c6baad5be2e00d569842123763b80507721ab87eb7af8735"
options = ["linkundefver"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libva-devel")
def _(self):
    return self.default_devel()
