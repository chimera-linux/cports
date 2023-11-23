pkgname = "c-ares"
pkgver = "1.22.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "C library for asynchronous DNS requests"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://c-ares.haxx.se"
source = f"https://c-ares.haxx.se/download/{pkgname}-{pkgver}.tar.gz"
sha256 = "f67c180deb799c670d9dda995a18ce06f6c7320b6c6363ff8fa85b77d0da9db8"
# FIXME cfi
hardening = ["vis", "!cfi"]
# does not like the sandbox
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("c-ares-devel")
def _devel(self):
    return self.default_devel()
