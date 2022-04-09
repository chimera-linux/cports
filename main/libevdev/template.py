pkgname = "libevdev"
pkgver = "1.12.1"
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
sha256 = "1dbba41bc516d3ca7abc0da5b862efe3ea8a7018fa6e9b97ce9d39401b22426c"

def post_install(self):
    self.install_license("COPYING")

@subpackage("libevdev-devel")
def _devel(self):
    self.depends += ["linux-headers"]
    return self.default_devel()

@subpackage("libevdev-progs")
def _progs(self):
    return self.default_progs()
