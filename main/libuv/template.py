pkgname = "libuv"
pkgver = "1.47.0"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
pkgdesc = "Multi-platform support library with focus on asynchronous I/O"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://libuv.org"
source = (
    f"https://dist.libuv.org/dist/v{pkgver}/{pkgname}-v{pkgver}-dist.tar.gz"
)
sha256 = "72a187104662b47f2a2b204da39d2acb05cf22a4fcb13ceaebe3b0ed0c0e2e43"
# FIXME cfi
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libuv-devel")
def _devel(self):
    return self.default_devel()
