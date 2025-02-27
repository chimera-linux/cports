pkgname = "rpcsvc-proto"
pkgver = "1.4.4"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
pkgdesc = "Rpcsvc protocol definitions from glibc"
license = "BSD-3-Clause"
url = "https://github.com/thkukuk/rpcsvc-proto"
source = f"{url}/releases/download/v{pkgver}/rpcsvc-proto-{pkgver}.tar.xz"
sha256 = "81c3aa27edb5d8a18ef027081ebb984234d5b5860c65bd99d4ac8f03145a558b"
options = ["!cross"]


def post_install(self):
    self.install_license("COPYING")
