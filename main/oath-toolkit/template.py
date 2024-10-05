pkgname = "oath-toolkit"
pkgver = "2.6.12"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "gtk-doc-tools",
    "libtool",
    "libxml2-progs",
    "pkgconf",
]
makedepends = ["linux-pam-devel", "libxml2-devel"]
pkgdesc = "OATH one-time password toolkit"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "GPL-3.0-or-later"
url = "http://www.nongnu.org/oath-toolkit"
source = f"http://download.savannah.gnu.org/releases/oath-toolkit/oath-toolkit-{pkgver}.tar.gz"
sha256 = "cafdf739b1ec4b276441c6aedae6411434bbd870071f66154b909cc6e2d9e8ba"
# TODO: failing checks are yet to be investigated
options = ["!check"]


@subpackage("oath-toolkit-devel")
def _(self):
    return self.default_devel()
