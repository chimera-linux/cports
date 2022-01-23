pkgname = "oniguruma"
pkgver = "6.9.7.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-posix-api=yes"]
hostmakedepends = ["pkgconf"]
pkgdesc = "Multi-charset regular expression library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/kkos/oniguruma"
source = f"{url}/releases/download/v{pkgver}/onig-{pkgver}.tar.gz"
sha256 = "6444204b9c34e6eb6c0b23021ce89a0370dad2b2f5c00cd44c342753e0b204d9"

def post_install(self):
    self.install_license("COPYING")

@subpackage("oniguruma-devel")
def _devel(self):
    return self.default_devel()
