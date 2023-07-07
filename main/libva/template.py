pkgname = "libva"
pkgver = "2.19.0"
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
source = f"https://github.com/intel/{pkgname}/archive/{pkgver}.tar.gz"
sha256 = "8cb5e2a9287a76b12c0b6cb96f4f27a0321bbe693df43cd950e5d4542db7f227"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libva-devel")
def _devel(self):
    return self.default_devel()
