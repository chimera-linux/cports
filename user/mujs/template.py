pkgname = "mujs"
pkgver = "1.3.5"
pkgrel = 0
build_style = "makefile"
make_install_target = (
    "install-shared"  # defaults to static otherwise, incompatible with cfi
)
make_install_args = ["prefix=/usr"]
hostmakedepends = ["pkgconf"]
makedepends = ["readline-devel"]  # TODO: editline
pkgdesc = "Embeddable Javascript interpreter"
maintainer = "ttyyls <contact@behri.org>"
license = "AGPL-3.0-or-later"
url = "https://mujs.com"
source = f"{url}/downloads/mujs-{pkgver}.tar.gz"
sha256 = "78a311ae4224400774cb09ef5baa2633c26971513f8b931d3224a0eb85b13e0b"
hardening = ["vis", "cfi"]
# no tests defined
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("mujs-devel")
def _(self):
    return self.default_devel()
