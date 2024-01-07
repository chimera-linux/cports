pkgname = "libexpat"
pkgver = "2.5.0"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--without-examples"]
configure_gen = []
make_check_args = ["-j1"]
hostmakedepends = ["pkgconf"]
pkgdesc = "XML parser library written in C"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://libexpat.github.io"
source = f"https://github.com/{pkgname}/{pkgname}/releases/download/R_{pkgver.replace('.', '_')}/expat-{pkgver}.tar.xz"
sha256 = "ef2420f0232c087801abf705e89ae65f6257df6b7931d37846a193ef2e8cdcbe"
# FIXME crash reproducible e.g. with graphene build
# FIXME visiility
hardening = ["!vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libexpat-devel")
def _devel(self):
    return self.default_devel()


@subpackage("xmlwf")
def _xmlwf(self):
    self.pkgdesc = f"{pkgdesc} (xmlwf utility)"
    return self.default_progs()
