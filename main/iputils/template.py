pkgname = "iputils"
pkgver = "20211215"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-DNO_SETCAP_OR_SUID=true",
    "-DUSE_IDN=false", 
    "-DBUILD_NINFOD=false"
]
hostmakedepends = [
    "meson", "pkgconf", "xsltproc", "docbook-xsl", "libcap-progs", "iproute2"
]
makedepends = ["libcap-devel"]
depends = ["libcap-progs"]
pkgdesc = "Useful utilities for Linux networking"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause AND GPL-2.0-or-later"
url = "https://github.com/iputils/iputils"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "b6f67fc705490673ff4471d006221b4a2f1b1180b929d9fefd771352621ccedf"
# operation not permitted (sandbox, unshared network)
options = ["!check"]

def post_install(self):
    self.install_license("Documentation/LICENSE.BSD3")
