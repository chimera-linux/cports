pkgname = "lsof"
pkgver = "4.99.3"
pkgrel = 2
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
maintainer = "psykose <alice@ayaya.dev>"
license = "custom:lsof"
url = "https://lsof.readthedocs.io/en/latest"
source = f"https://github.com/lsof-org/lsof/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "b9c56468b927d9691ab168c0b1e9f8f1f835694a35ff898c549d383bd8d09bd4"
patch_style = "patch"
hardening = ["vis", "!cfi"]
# FIXME: weird failures
options = ["!check"]
exec_wrappers = [("/usr/bin/mandoc", "nroff")]


def post_install(self):
    self.install_license("COPYING")


@subpackage("lsof-devel")
def _(self):
    return self.default_devel()
