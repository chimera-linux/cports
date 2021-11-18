pkgname = "libevdev"
pkgver = "1.12.0"
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
sha256 = "2f729e3480695791f9482e8388bd723402b89f0eaf118057bbdea3cecee9b237"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libevdev-devel")
def _devel(self):
    self.depends += ["linux-headers"]
    return self.default_devel(man = True)

@subpackage("libevdev-progs")
def _progs(self):
    return self.default_progs()
