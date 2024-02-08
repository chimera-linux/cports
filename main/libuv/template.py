pkgname = "libuv"
pkgver = "1.48.0"
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
sha256 = "c593139feb9061699fdd2f7fde47bb6c1ca77761ae9ec04f052083f1ef46c13b"
# FIXME cfi
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libuv-devel")
def _devel(self):
    return self.default_devel()
