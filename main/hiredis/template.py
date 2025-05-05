pkgname = "hiredis"
pkgver = "1.3.0"
pkgrel = 0
build_style = "makefile"
make_build_args = ["USE_SSL=1"]
make_install_args = ["USE_SSL=1"]
hostmakedepends = ["pkgconf"]
makedepends = ["openssl3-devel"]
pkgdesc = "Minimalistic C client library for Redis"
license = "BSD-3-Clause"
url = "https://github.com/redis/hiredis"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "25cee4500f359cf5cad3b51ed62059aadfc0939b05150c1f19c7e2829123631c"
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
