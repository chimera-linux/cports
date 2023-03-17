pkgname = "hiredis"
pkgver = "1.1.0"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_args = ["USE_SSL=1"]
make_install_args = ["USE_SSL=1"]
hostmakedepends = ["pkgconf", "gmake"]
makedepends = ["openssl-devel"]
pkgdesc = "Minimalistic C client library for Redis"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/redis/hiredis"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "fe6d21741ec7f3fc9df409d921f47dfc73a4d8ff64f4ac6f1d95f951bf7f53d6"
# needs redis
options = ["!check"]

def init_configure(self):
    self.make_build_args += ["DEBUG=" + self.get_cflags(shell = True)]

def post_install(self):
    self.install_license("COPYING")

@subpackage("hiredis-ssl")
def _ssl(self):
    self.pkgdesc = f"{pkgdesc} (hiredis_ssl library)"

    return ["usr/lib/libhiredis_ssl.so.*"]

@subpackage("hiredis-devel")
def _devel(self):
    return self.default_devel()
