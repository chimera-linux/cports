pkgname = "lsof"
pkgver = "4.99.4"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "mandoc",
    "pkgconf",
]
makedepends = ["linux-headers"]
checkdepends = ["bash"]
pkgdesc = "List open files"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "custom:lsof"
url = "https://lsof.readthedocs.io/en/latest"
source = f"https://github.com/lsof-org/lsof/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "90d02ae35cd14341bfb04ce80e0030767476b0fc414a0acb115d49e79b13d56c"
hardening = ["vis", "!cfi"]
# FIXME: weird failures
options = ["!check"]
exec_wrappers = [("/usr/bin/mandoc", "nroff")]


def post_install(self):
    self.install_license("COPYING")


@subpackage("lsof-devel")
def _(self):
    return self.default_devel()
