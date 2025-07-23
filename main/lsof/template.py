pkgname = "lsof"
pkgver = "4.99.5"
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
sha256 = "3c591556c665196e0aada5982ff43c75e248187bad78bb1368d8fb9c1c527e6e"
hardening = ["vis", "!cfi"]
# FIXME: weird failures
options = ["!check"]
exec_wrappers = [("/usr/bin/mandoc", "nroff")]


def post_install(self):
    self.install_license("COPYING")


@subpackage("lsof-devel")
def _(self):
    return self.default_devel()
