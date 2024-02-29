pkgname = "libexpat"
pkgver = "2.6.1"
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
sha256 = "0c00d2760ad12efef6e26efc8b363c8eb28eb8c8de719e46d5bb67b40ba904a3"
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
