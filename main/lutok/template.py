pkgname = "lutok"
pkgver = "0.6.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-atf=no"]
make_dir = "."
hostmakedepends = ["atf-devel", "automake", "libtool", "pkgconf"]
makedepends = ["lua5.4-devel"]
pkgdesc = "C++ API for Lua"
license = "BSD-3-Clause"
url = "https://github.com/freebsd/lutok"
source = f"{url}/archive/refs/tags/lutok-{pkgver}.tar.gz"
sha256 = "32bdd78b836598ff7c33487e8328ec7a0ca7fcf8356b777edfc84d1525516e87"
# Cycle with kyua
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("lutok-devel")
def _(self):
    self.depends += ["lua5.4-devel"]

    return self.default_devel()
