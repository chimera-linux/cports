pkgname = "libevdev"
pkgver = "1.13.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-gcov"]
hostmakedepends = ["pkgconf", "python", "automake", "libtool"]
makedepends = ["check-devel", "linux-headers"]
checkdepends = ["bash"]
pkgdesc = "Wrapper library for evdev devices"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.freedesktop.org/wiki/Software/libevdev"
source = f"$(FREEDESKTOP_SITE)/libevdev/libevdev-{pkgver}.tar.xz"
sha256 = "abf1aace86208eebdd5d3550ffded4c8d73bb405b796d51c389c9d0604cbcfbf"
# FIXME int
hardening = ["!int"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libevdev-devel")
def _(self):
    self.depends += ["linux-headers"]
    return self.default_devel()


@subpackage("libevdev-progs")
def _(self):
    return self.default_progs()
