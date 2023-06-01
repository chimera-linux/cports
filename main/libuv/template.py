pkgname = "libuv"
pkgver = "1.45.0"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["pkgconf"]
pkgdesc = "Multi-platform support library with focus on asynchronous I/O"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://libuv.org"
source = f"https://dist.libuv.org/dist/v{pkgver}/{pkgname}-v{pkgver}-dist.tar.gz"
sha256 = "3793d8c0d6fa587721d010d0555b7e82443fd4e8b3c91e529eb6607592f52b87"
# FIXME cfi
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libuv-devel")
def _devel(self):
    return self.default_devel()
