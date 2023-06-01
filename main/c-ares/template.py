pkgname = "c-ares"
pkgver = "1.19.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "C library for asynchronous DNS requests"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://c-ares.haxx.se"
source = f"https://c-ares.haxx.se/download/{pkgname}-{pkgver}.tar.gz"
sha256 = "321700399b72ed0e037d0074c629e7741f6b2ec2dda92956abe3e9671d3e268e"
# FIXME cfi
hardening = ["vis", "!cfi"]
# does not like the sandbox
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("c-ares-devel")
def _devel(self):
    return self.default_devel()
