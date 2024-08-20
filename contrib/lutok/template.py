pkgname = "lutok"
pkgver = "0.4"
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
source = f"{url}/releases/download/lutok-{pkgver}/lutok-{pkgver}.tar.gz"
sha256 = "2cec51efa0c8d65ace8b21eaa08384b77abc5087b46e785f78de1c21fb754cd5"
tool_flags = {"CXXFLAGS": ["-std=gnu++11"]}
# Cycle with kyua
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("lutok-devel")
def _(self):
    self.depends += ["lua5.4-devel"]

    return self.default_devel()
