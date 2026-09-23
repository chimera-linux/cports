pkgname = "libva"
pkgver = "2.24.1"
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
sha256 = "0b4a3649ee8d683b9cce2ef094df4fb039d276c0cef7e49337c43d3b297b9f42"
options = ["linkundefver"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libva-devel")
def _(self):
    return self.default_devel()
