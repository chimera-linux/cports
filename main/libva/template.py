pkgname = "libva"
pkgver = "2.15.0"
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
sha256 = "869aaa9b9eccb1cde63e1c5b0ac0881cefc00156010bb49f6dce152471770ba8"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libva-devel")
def _devel(self):
    return self.default_devel()
