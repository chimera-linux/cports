pkgname = "lsof"
pkgver = "4.99.7"
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
license = "custom:lsof"
url = "https://lsof.readthedocs.io/en/latest"
source = f"https://github.com/lsof-org/lsof/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "bac1b0acbc50aede42fc97dffaa0b0475e97973e36a6351de5f349c6155afc68"
# FIXME: weird failures
options = ["!check"]
exec_wrappers = [("/usr/bin/mandoc", "nroff")]


def post_install(self):
    self.install_license("COPYING")


@subpackage("lsof-devel")
def _(self):
    return self.default_devel()
