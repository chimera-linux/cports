pkgname = "libevdev"
pkgver = "1.13.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-gcov"]
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf", "python", "automake", "libtool"]
makedepends = ["check-devel", "linux-headers"]
checkdepends = ["bash"]
pkgdesc = "Wrapper library for evdev devices"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.freedesktop.org/wiki/Software/libevdev"
source = f"$(FREEDESKTOP_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "06a77bf2ac5c993305882bc1641017f5bec1592d6d1b64787bad492ab34f2f36"
# FIXME int
hardening = ["!int"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libevdev-devel")
def _devel(self):
    self.depends += ["linux-headers"]
    return self.default_devel()


@subpackage("libevdev-progs")
def _progs(self):
    return self.default_progs()
