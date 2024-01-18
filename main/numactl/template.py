pkgname = "numactl"
pkgver = "2.0.17"
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
sha256 = "af22829cda8b5bdee3d280e61291697bbd3f9bd372afdf119c9348b88369d40b"
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
