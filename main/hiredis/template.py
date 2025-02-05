pkgname = "hiredis"
pkgver = "1.2.0"
pkgrel = 0
build_style = "makefile"
make_build_args = ["USE_SSL=1"]
make_install_args = ["USE_SSL=1"]
hostmakedepends = ["pkgconf"]
makedepends = ["openssl3-devel"]
pkgdesc = "Minimalistic C client library for Redis"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/redis/hiredis"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "82ad632d31ee05da13b537c124f819eb88e18851d9cb0c30ae0552084811588c"
# needs redis
options = ["!check"]


def init_configure(self):
    self.make_build_args += ["DEBUG=" + self.get_cflags(shell=True)]


def post_install(self):
    self.install_license("COPYING")


@subpackage("hiredis-ssl")
def _(self):
    self.subdesc = "hiredis_ssl library"

    return ["usr/lib/libhiredis_ssl.so.*"]


@subpackage("hiredis-devel")
def _(self):
    return self.default_devel()
