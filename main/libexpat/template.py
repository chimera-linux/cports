pkgname = "libexpat"
pkgver = "2.6.2"
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
sha256 = "ee14b4c5d8908b1bec37ad937607eab183d4d9806a08adee472c3c3121d27364"
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
