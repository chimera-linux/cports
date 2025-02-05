pkgname = "numactl"
pkgver = "2.0.19"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["linux-headers"]
checkdepends = ["bash"]
pkgdesc = "Simple NUMA policy support"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-only"
url = "https://github.com/numactl/numactl"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "8b84ffdebfa0d730fb2fc71bb7ec96bb2d38bf76fb67246fde416a68e04125e4"
# some tests fail because of gnuisms in testsuite
options = ["!check"]


def post_install(self):
    self.uninstall("usr/share/man/man2")


@subpackage("numactl-libs")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libnuma")]

    return self.default_libs()


@subpackage("numactl-devel")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libnuma-devel")]

    return self.default_devel()
