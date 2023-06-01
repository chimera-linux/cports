pkgname = "libinput"
pkgver = "1.23.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddocumentation=false",
    "-Dtests=true",
    "-Ddebug-gui=false",
    "-Db_ndebug=false",
]
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "libevdev-devel",
    "mtdev-devel",
    "udev-devel",
    "libwacom-devel",
]
checkdepends = ["check-devel", "python-pytest", "bash"]
pkgdesc = "Input abstraction library for Wayland and X"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.freedesktop.org/wiki/Software/libinput"
source = f"https://gitlab.freedesktop.org/{pkgname}/{pkgname}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "7a7c90fbc59f1f65c781a51fa634e4f79e460bf6e16ad68afbe7965d25d09738"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libinput-devel")
def _devel(self):
    self.depends += makedepends
    return self.default_devel()
