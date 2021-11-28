pkgname = "iputils"
pkgver = "20210722"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-DNO_SETCAP_OR_SUID=true",
    "-DUSE_IDN=false", 
    "-DBUILD_TFTPD=false",
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
sha256 = "6d1a44b0682d3d4b64586dbaebe61dd61ae16d6e2f4dc0c43336d0e47a9db323"
# operation not permitted (sandbox, unshared network)
options = ["!check", "lto"]

def post_install(self):
    self.install_license("Documentation/LICENSE.BSD3")
