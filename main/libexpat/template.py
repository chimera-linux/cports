pkgname = "libexpat"
pkgver = "2.8.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--without-examples"]
configure_gen = []
make_check_args = ["-j1"]
hostmakedepends = ["pkgconf"]
pkgdesc = "Stream-oriented XML parser library"
license = "MIT"
url = "https://libexpat.github.io"
source = f"https://github.com/libexpat/libexpat/releases/download/R_{pkgver.replace('.', '_')}/expat-{pkgver}.tar.xz"
sha256 = "656ae1cc8da3b4ea513bb4e254f33e6243938084c0ec6239da873376b09985a7"
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
