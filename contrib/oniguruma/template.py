pkgname = "oniguruma"
pkgver = "6.9.8"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-posix-api=yes"]
hostmakedepends = ["pkgconf"]
pkgdesc = "Multi-charset regular expression library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/kkos/oniguruma"
source = f"{url}/releases/download/v{pkgver}/onig-{pkgver}.tar.gz"
sha256 = "28cd62c1464623c7910565fb1ccaaa0104b2fe8b12bcd646e81f73b47535213e"

def post_install(self):
    self.install_license("COPYING")

@subpackage("oniguruma-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []
