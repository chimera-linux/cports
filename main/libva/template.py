pkgname = "libva"
pkgver = "2.17.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dwith_glx=yes", "-Dwith_wayland=yes"]
hostmakedepends = ["meson", "pkgconf", "wayland-progs"]
makedepends = [
    "libxfixes-devel", "libxext-devel", "libdrm-devel", "libffi-devel",
    "wayland-devel", "mesa-devel"
]
pkgdesc = "Video Acceleration API"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://01.org/linuxmedia/vaapi"
source = f"https://github.com/intel/{pkgname}/archive/{pkgver}.tar.gz"
sha256 = "8940541980ef998a36cd8f6ad905e81838ea4ddf56dc479ed2bebd12711e6001"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libva-devel")
def _devel(self):
    return self.default_devel()
