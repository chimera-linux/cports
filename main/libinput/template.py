pkgname = "libinput"
pkgver = "1.24.0"
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
sha256 = "7413c3733b8c39dc38b8687950e0e0d9d38a73394539f9efa2a7c84a412cb505"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libinput-devel")
def _devel(self):
    self.depends += makedepends
    return self.default_devel()
