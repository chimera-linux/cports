pkgname = "libuv"
pkgver = "1.49.2"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
pkgdesc = "Multi-platform support library with focus on asynchronous I/O"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://libuv.org"
source = f"https://dist.libuv.org/dist/v{pkgver}/libuv-v{pkgver}-dist.tar.gz"
sha256 = "2e910e668e5daf1be6a5195a696985d7200adfa5c4d3400ee7b3355affdcf52c"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libuv-devel")
def _(self):
    return self.default_devel()
