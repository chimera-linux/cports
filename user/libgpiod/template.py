pkgname = "libgpiod"
pkgver = "2.2.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--enable-tools=yes",
]
hostmakedepends = [
    "autoconf-archive",
    "automake",
    "linux-headers",
    "pkgconf",
    "slibtool",
]
pkgdesc = "C library and tools for the linux GPIO character device"
license = "LGPL-2.1-or-later"
url = "https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git"
source = f"{url}/snapshot/libgpiod-{pkgver}.tar.gz"
sha256 = "d0b1380c3cbabbb49b82f709b3288376d98347d4436613407d19cc4cbbfc45a6"


def post_install(self):
    self.install_license("COPYING")


@subpackage("libgpiod-devel")
def _(self):
    return self.default_devel()
