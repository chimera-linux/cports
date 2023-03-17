pkgname = "iputils"
pkgver = "20221126"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-DNO_SETCAP_OR_SUID=true",
    "-DUSE_IDN=false", 
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
sha256 = "745ea711fe06d5c57d470d21acce3c3ab866eb6afb69379a16c6d60b89bd4311"
hardening = ["vis", "cfi"]
# operation not permitted (sandbox, unshared network)
options = ["!check"]

def post_install(self):
    self.install_license("Documentation/LICENSE.BSD3")
