pkgname = "libexpat"
pkgver = "2.6.0"
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
sha256 = "cb5f5a8ea211e1cabd59be0a933a52e3c02cc326e86a4d387d8d218e7ee47a3e"
# FIXME crash reproducible e.g. with graphene build
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libexpat-devel")
def _devel(self):
    return self.default_devel()


@subpackage("xmlwf")
def _xmlwf(self):
    self.pkgdesc = f"{pkgdesc} (xmlwf utility)"
    return self.default_progs()
