pkgname = "libuv"
pkgver = "1.44.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "Multi-platform support library with focus on asynchronous I/O"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://libuv.org"
# autogen.sh && configure && make dist
source = f"https://repo.chimera-linux.org/distfiles/{pkgname}-{pkgver}.tar.gz"
sha256 = "751a1ccdb74197593d68ab04f34aa2cfa23832614d8f8161f4ecc7f179d51bc3"
# FIXME cfi
hardening = ["vis", "!cfi"]

def post_install(self):
    self.install_license("LICENSE")

@subpackage("libuv-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []
