pkgname = "lsof"
pkgver = "4.99.0"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "groff",
    "gmake",
    "libtool",
    "pkgconf",
]
makedepends = ["linux-headers"]
checkdepends = ["bash"]
pkgdesc = "List open files"
maintainer = "psykose <alice@ayaya.dev>"
license = "custom:lsof"
url = "https://lsof.readthedocs.io/en/latest"
source = f"https://github.com/lsof-org/lsof/releases/download/{pkgver}/lsof-{pkgver}.tar.gz"
sha256 = "180e6284aff184d94d273e34f7264edc2af849c07b1c5d6a4183d4d402734245"
# FIXME: cfi
hardening = ["vis"]
# FIXME: weird failures
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("lsof-devel")
def _devel(self):
    return self.default_devel()
