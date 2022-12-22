pkgname = "libva"
pkgver = "2.16.0"
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
sha256 = "766edf51fd86efe9e836a4467d4ec7c3af690a3c601b3c717237cee856302279"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libva-devel")
def _devel(self):
    return self.default_devel()

# FIXME visibility
hardening = ["!vis"]
