pkgname = "libevdev"
pkgver = "1.11.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-gcov"]
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf", "python"]
makedepends = ["check-devel", "linux-headers"]
checkdepends = ["bash"]
pkgdesc = "Wrapper library for evdev devices"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.freedesktop.org/wiki/Software/libevdev"
source = f"$(FREEDESKTOP_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "63f4ea1489858a109080e0b40bd43e4e0903a1e12ea888d581db8c495747c2d0"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libevdev-devel")
def _devel(self):
    self.depends += ["linux-headers"]
    return self.default_devel(man = True)

@subpackage("libevdev-progs")
def _progs(self):
    return self.default_progs()
