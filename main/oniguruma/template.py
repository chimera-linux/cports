pkgname = "oniguruma"
pkgver = "6.9.9"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-posix-api=yes"]
hostmakedepends = ["automake", "libtool", "pkgconf"]
pkgdesc = "Multi-charset regular expression library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/kkos/oniguruma"
source = f"{url}/releases/download/v{pkgver}/onig-{pkgver}.tar.gz"
sha256 = "60162bd3b9fc6f4886d4c7a07925ffd374167732f55dce8c491bfd9cd818a6cf"


def post_install(self):
    self.install_license("COPYING")


@subpackage("oniguruma-devel")
def _(self):
    return self.default_devel()
