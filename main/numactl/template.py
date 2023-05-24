pkgname = "numactl"
pkgver = "2.0.16"
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
sha256 = "a35c3bdb3efab5c65927e0de5703227760b1101f5e27ab741d8f32b3d5f0a44c"
# some tests fail because of gnuisms in testsuite
options = ["!check"]


def post_install(self):
    self.rm(self.destdir / "usr/share/man/man2", recursive=True)


@subpackage("libnuma")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()


@subpackage("libnuma-devel")
def _devel(self):
    return self.default_devel()
