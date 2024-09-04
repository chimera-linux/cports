pkgname = "libexpat"
pkgver = "2.6.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--without-examples"]
configure_gen = []
make_check_args = ["-j1"]
hostmakedepends = ["pkgconf"]
pkgdesc = "XML parser library written in C"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://libexpat.github.io"
source = f"https://github.com/libexpat/libexpat/releases/download/R_{pkgver.replace('.', '_')}/expat-{pkgver}.tar.xz"
sha256 = "274db254a6979bde5aad404763a704956940e465843f2a9bd9ed7af22e2c0efc"
# CFI: crash reproducible e.g. with graphene build
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libexpat-devel")
def _(self):
    return self.default_devel()


@subpackage("xmlwf")
def _(self):
    self.subdesc = "xmlwf utility"
    return self.default_progs()
