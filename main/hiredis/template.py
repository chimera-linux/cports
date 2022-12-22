pkgname = "hiredis"
pkgver = "1.0.2"
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
sha256 = "e0ab696e2f07deb4252dda45b703d09854e53b9703c7d52182ce5a22616c3819"
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

# FIXME visibility
hardening = ["!vis"]
