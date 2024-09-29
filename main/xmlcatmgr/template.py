pkgname = "xmlcatmgr"
pkgver = "2.2"
pkgrel = 4
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool"]
triggers = [
    "/usr/share/xml/catalogs",
    "/usr/share/sgml/catalogs",
]
pkgdesc = "XML and SGML catalog manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "http://xmlcatmgr.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/xmlcatmgr/xmlcatmgr-{pkgver}.tar.gz"
sha256 = "ea1142b6aef40fbd624fc3e2130cf10cf081b5fa88e5229c92b8f515779d6fdc"
file_modes = {
    "+usr/share/xml/catalogs": ("root", "root", 0o755, True),
    "+usr/share/sgml/catalogs": ("root", "root", 0o755, True),
}
# ld: error: undefined symbol: setprogname
options = ["!lto"]


def post_install(self):
    self.install_license("COPYING")
