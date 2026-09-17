pkgname = "libevdev"
pkgver = "1.13.7"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-gcov"]
hostmakedepends = ["pkgconf", "python", "automake", "libtool"]
makedepends = ["check-devel", "linux-headers"]
checkdepends = ["bash"]
pkgdesc = "Wrapper library for evdev devices"
license = "MIT"
url = "https://www.freedesktop.org/wiki/Software/libevdev"
source = f"$(FREEDESKTOP_SITE)/libevdev/libevdev-{pkgver}.tar.xz"
sha256 = "0caf824971108f15bb2ad356433bae198d7d3bf1e82d43f63626e069e060bfa6"
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
