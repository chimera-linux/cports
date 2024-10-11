pkgname = "libuv"
pkgver = "1.49.1"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
pkgdesc = "Multi-platform support library with focus on asynchronous I/O"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://libuv.org"
source = f"https://dist.libuv.org/dist/v{pkgver}/libuv-v{pkgver}-dist.tar.gz"
sha256 = "a4fc48e8972a9665c3ef0a585a572e5bd4b741b7d0f06326b340d7bd4106b874"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libuv-devel")
def _(self):
    return self.default_devel()
