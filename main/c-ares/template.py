pkgname = "c-ares"
pkgver = "1.21.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "automake", "libtool"]
pkgdesc = "C library for asynchronous DNS requests"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://c-ares.haxx.se"
source = f"https://c-ares.haxx.se/download/{pkgname}-{pkgver}.tar.gz"
sha256 = "cd7aa3af1d3ee780d6437039a7ddb7f1ec029f9c4f7aabb0197e384eb5bc2f2d"
# FIXME cfi
hardening = ["vis", "!cfi"]
# does not like the sandbox
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("c-ares-devel")
def _devel(self):
    return self.default_devel()
