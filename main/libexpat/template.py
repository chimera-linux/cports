pkgname = "libexpat"
pkgver = "2.8.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--without-examples"]
configure_gen = []
make_check_args = ["-j1"]
hostmakedepends = ["pkgconf"]
pkgdesc = "XML parser library written in C"
license = "MIT"
url = "https://libexpat.github.io"
source = f"https://github.com/libexpat/libexpat/releases/download/R_{pkgver.replace('.', '_')}/expat-{pkgver}.tar.xz"
sha256 = "a37bfae0aa9775bd8521ebd85dc456d486f0ff31138f6c91fd902ea732624542"
# CFI: crash reproducible e.g. with graphene build
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libexpat-devel")
def _(self):
    return self.default_devel()


@subpackage("libexpat-progs")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("xmlwf")]

    return self.default_progs()
