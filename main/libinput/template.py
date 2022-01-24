pkgname = "libinput"
pkgver = "1.19.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddocumentation=false", "-Dtests=true",
    "-Ddebug-gui=false", "-Db_ndebug=false"
]
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "libevdev-devel", "mtdev-devel", "eudev-devel", "libwacom-devel",
]
checkdepends = ["check-devel", "bash"]
pkgdesc = "Input abstraction library for Wayland and X"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.freedesktop.org/wiki/Software/libinput"
source = f"$(FREEDESKTOP_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "0fc39f0af3ee1a77c60c34bc45391a4d0879169f7c0f7bbbeb5eef590b98b883"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libinput-devel")
def _devel(self):
    self.depends += makedepends
    return self.default_devel()
