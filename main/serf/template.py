pkgname = "serf"
pkgver = "1.3.10"
pkgrel = 0
hostmakedepends = ["pkgconf", "scons"]
makedepends = ["apr-util-devel", "openssl3-devel", "zlib-ng-compat-devel"]
pkgdesc = "Asynchronous HTTP client library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://serf.apache.org"
source = f"https://archive.apache.org/dist/serf/serf-{pkgver}.tar.bz2"
sha256 = "be81ef08baa2516ecda76a77adf7def7bc3227eeb578b9a33b45f7b41dc064e6"
# not even once
options = ["!cross"]


def build(self):
    self.do(
        "scons",
        "CFLAGS=" + self.get_cflags(shell=True),
        "LINKFLAGS=" + self.get_ldflags(shell=True),
        "PREFIX=/usr",
    )


def install(self):
    self.do("scons", "install", f"--install-sandbox={self.chroot_destdir}")


@subpackage("serf-devel")
def _(self):
    return self.default_devel()
