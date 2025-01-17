pkgname = "libuv"
pkgver = "1.50.0"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
pkgdesc = "Multi-platform support library with focus on asynchronous I/O"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://libuv.org"
source = f"https://dist.libuv.org/dist/v{pkgver}/libuv-v{pkgver}-dist.tar.gz"
sha256 = "c42c51d4e630f95dcefcafff95bf003ea52939e312d5e6584e7d9e102ead3e9e"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libuv-devel")
def _(self):
    return self.default_devel()
