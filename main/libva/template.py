pkgname = "libva"
pkgver = "2.23.0"
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
sha256 = "b10aceb30e93ddf13b2030eb70079574ba437be9b3b76065caf28a72c07e23e7"
options = ["linkundefver"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libva-devel")
def _(self):
    return self.default_devel()
