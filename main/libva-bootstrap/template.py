pkgname = "libva-bootstrap"
pkgver = "2.17.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddefault_library=shared",
    "-Dwith_glx=no", "-Dwith_x11=no", "-Dwith_wayland=no",
]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["libffi-devel", "libdrm-devel"]
# no provides needed, only for mesa which needs headers
pkgdesc = "Video Acceleration API (bootstrap)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://01.org/linuxmedia/vaapi"
source = f"https://github.com/intel/libva/archive/{pkgver}.tar.gz"
sha256 = "8940541980ef998a36cd8f6ad905e81838ea4ddf56dc479ed2bebd12711e6001"
options = ["!lto", "!scanshlibs", "!scanpkgconf"]

def post_install(self):
    self.install_license("COPYING")
