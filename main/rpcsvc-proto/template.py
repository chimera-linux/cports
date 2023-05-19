pkgname = "rpcsvc-proto"
pkgver = "1.4.3"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["gmake"]
pkgdesc = "Rpcsvc protocol definitions from glibc"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/thkukuk/rpcsvc-proto"
source = f"{url}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "69315e94430f4e79c74d43422f4a36e6259e97e67e2677b2c7d7060436bd99b1"
options = ["!cross"]

def post_install(self):
    self.install_license("COPYING")

configure_gen = []
