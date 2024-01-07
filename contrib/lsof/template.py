pkgname = "lsof"
pkgver = "4.99.3"
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
source = f"https://github.com/lsof-org/lsof/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "b9c56468b927d9691ab168c0b1e9f8f1f835694a35ff898c549d383bd8d09bd4"
# FIXME: cfi
hardening = ["vis"]
# FIXME: weird failures
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("lsof-devel")
def _devel(self):
    return self.default_devel()
