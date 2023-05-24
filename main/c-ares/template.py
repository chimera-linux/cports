pkgname = "c-ares"
pkgver = "1.19.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "C library for asynchronous DNS requests"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://c-ares.haxx.se"
source = f"https://c-ares.haxx.se/download/{pkgname}-{pkgver}.tar.gz"
sha256 = "bfceba37e23fd531293829002cac0401ef49a6dc55923f7f92236585b7ad1dd3"
# FIXME cfi
hardening = ["vis", "!cfi"]
# does not like the sandbox
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("c-ares-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
