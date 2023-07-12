pkgname = "libuv"
pkgver = "1.46.0"
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
sha256 = "94f101111ef3209340d7f09c2aa150ddb4feabd2f9d87d47d9f5bded835b8094"
# FIXME cfi
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libuv-devel")
def _devel(self):
    return self.default_devel()
