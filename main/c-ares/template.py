pkgname = "c-ares"
pkgver = "1.18.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
checkdepends = ["iana-etc"]
pkgdesc = "C library for asynchronous DNS requests"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://c-ares.haxx.se"
source = f"https://c-ares.haxx.se/download/{pkgname}-{pkgver}.tar.gz"
sha256 = "1a7d52a8a84a9fbffb1be9133c0f6e17217d91ea5a6fa61f6b4729cda78ebbcf"
# FIXME cfi
hardening = ["vis", "!cfi"]
# does not like the sandbox
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE.md")

@subpackage("c-ares-devel")
def _devel(self):
    return self.default_devel()
