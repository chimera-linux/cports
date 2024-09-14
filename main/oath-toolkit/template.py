pkgname = "oath-toolkit"
pkgver = "2.6.11"
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
sha256 = "fc512a4a5b46f4c43ab0586c3189fece4d54f7e649397d6fa1e23428431e2cb4"
# TODO: failing checks are yet to be investigated
options = ["!check"]


@subpackage("oath-toolkit-devel")
def _(self):
    return self.default_devel()
