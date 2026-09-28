pkgname = "libslirp"
pkgver = "4.9.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["glib-devel", "linux-headers"]
pkgdesc = "General purpose TCP-IP emulator"
license = "BSD-3-Clause"
url = "https://gitlab.freedesktop.org/slirp/libslirp"
source = f"{url}/-/archive/v{pkgver}/libslirp-v{pkgver}.tar.gz"
sha256 = "e744a32767668fe80e3cb3bd75d10d501f981e98c26a1f318154a97e99cdac22"
options = ["linkundefver"]


def post_install(self):
    self.install_license("COPYRIGHT")


@subpackage("libslirp-devel")
def _(self):
    return self.default_devel()
