pkgname = "lutok"
pkgver = "0.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-atf=no"]
make_dir = "."
hostmakedepends = ["atf-devel", "automake", "libtool", "pkgconf"]
makedepends = ["lua5.4-devel"]
pkgdesc = "C++ API for Lua"
maintainer = "triallax <triallax@tutanota.com>"
license = "BSD-3-Clause"
url = "https://github.com/freebsd/lutok"
source = f"{url}/archive/refs/tags/lutok-{pkgver}.tar.gz"
sha256 = "fea79b79e80a9787143a1d4d5e4962d061ff7923efe6b2ba3a332b25a9b31f72"
# Cycle with kyua
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("lutok-devel")
def _(self):
    self.depends += ["lua5.4-devel"]

    return self.default_devel()
