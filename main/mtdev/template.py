pkgname = "mtdev"
pkgver = "1.1.7"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["linux-headers"]
pkgdesc = "Multitouch Protocol Translation Library"
license = "MIT"
url = "https://bitmath.org/code/mtdev"
source = f"{url}/mtdev-{pkgver}.tar.bz2"
sha256 = "a107adad2101fecac54ac7f9f0e0a0dd155d954193da55c2340c97f2ff1d814e"


def post_install(self):
    self.install_license("COPYING")


@subpackage("mtdev-devel")
def _(self):
    self.depends += ["linux-headers"]
    return self.default_devel()
