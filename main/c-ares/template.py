pkgname = "c-ares"
pkgver = "1.17.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
checkdepends = ["iana-etc"]
pkgdesc = "C library for asynchronous DNS requests"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://c-ares.haxx.se"
source = f"https://c-ares.haxx.se/download/{pkgname}-{pkgver}.tar.gz"
sha256 = "4803c844ce20ce510ef0eb83f8ea41fa24ecaae9d280c468c582d2bb25b3913d"
# does not like the sandbox
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE.md")

@subpackage("c-ares-devel")
def _devel(self):
    return self.default_devel(man = True)
