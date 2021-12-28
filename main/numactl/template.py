pkgname = "numactl"
pkgver = "2.0.14"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["automake", "libtool", "pkgconf", "gmake"]
makedepends = ["linux-headers"]
checkdepends = ["bash"]
pkgdesc = "Simple NUMA policy support"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-only"
url = "https://github.com/numactl/numactl"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "1ee27abd07ff6ba140aaf9bc6379b37825e54496e01d6f7343330cf1a4487035"
# some tests fail because of gnuisms in testsuite
options = ["!check"]

def pre_configure(self):
    self.do("autoreconf", "-if")

def post_install(self):
    self.rm(self.destdir / "usr/share/man/man2", recursive = True)

@subpackage("libnuma")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()

@subpackage("libnuma-devel")
def _devel(self):
    return self.default_devel()
