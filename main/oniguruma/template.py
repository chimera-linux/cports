pkgname = "oniguruma"
pkgver = "6.9.10"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-posix-api=yes"]
hostmakedepends = ["automake", "libtool", "pkgconf"]
pkgdesc = "Multi-charset regular expression library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/kkos/oniguruma"
source = f"{url}/releases/download/v{pkgver}/onig-{pkgver}.tar.gz"
sha256 = "2a5cfc5ae259e4e97f86b68dfffc152cdaffe94e2060b770cb827238d769fc05"


def post_install(self):
    self.install_license("COPYING")


@subpackage("oniguruma-devel")
def _(self):
    return self.default_devel()
