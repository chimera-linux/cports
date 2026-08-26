pkgname = "libuv"
pkgver = "1.52.1"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["linux-headers"]
pkgdesc = "Multi-platform support library with focus on asynchronous I/O"
license = "MIT"
url = "https://libuv.org"
source = f"https://dist.libuv.org/dist/v{pkgver}/libuv-v{pkgver}-dist.tar.gz"
sha256 = "c5f14915e2fa7b83b6111c3bc477920559499e10d95f852707420c8725b82d6a"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libuv-devel")
def _(self):
    return self.default_devel()
