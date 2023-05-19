pkgname = "xmlcatmgr"
pkgver = "2.2"
pkgrel = 0
build_style = "gnu_configure"
pkgdesc = "XML and SGML catalog manager"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "http://xmlcatmgr.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/xmlcatmgr/{pkgname}-{pkgver}.tar.gz"
sha256 = "ea1142b6aef40fbd624fc3e2130cf10cf081b5fa88e5229c92b8f515779d6fdc"
# ld: error: undefined symbol: setprogname
options = ["!lto"]

if self.profile().cross:
    hostmakedepends += ["xmlcatmgr"]

def post_build(self):
    if self.profile().cross:
        xcmgr = "/usr/bin/xmlcatmgr"
    else:
        xcmgr = self.chroot_cwd / self.make_dir / "xmlcatmgr"

    self.log("creating SGML catalogs...")
    self.do(xcmgr, "-sc", "catalog.etc.sgml", "create")
    self.do(xcmgr, "-sc", "catalog.sgml", "create")
    self.do(
        xcmgr, "-sc", "catalog.etc.sgml", "add", "CATALOG",
        "/etc/sgml/auto/catalog"
    )

    self.log("creating XML catalogs...")
    self.do(xcmgr, "-c", "catalog.etc.xml", "create")
    self.do(xcmgr, "-c", "catalog.xml", "create")
    self.do(
        xcmgr, "-c", "catalog.etc.xml", "add", "nextCatalog",
        "/etc/xml/auto/catalog"
    )

def post_install(self):
    self.log("installing XML/SGML catalogs...")

    self.install_file("catalog.sgml", "etc/sgml/auto", name = "catalog")
    self.install_file("catalog.etc.sgml", "etc/sgml", name = "catalog")
    self.install_file("catalog.xml", "etc/xml/auto", name = "catalog")
    self.install_file("catalog.etc.xml", "etc/xml", name = "catalog")

    self.install_dir("usr/share/sgml")
    self.install_dir("usr/share/xml")
    self.install_link("/etc/sgml/auto/catalog", "usr/share/sgml/catalog")
    self.install_link("/etc/xml/auto/catalog", "usr/share/xml/catalog")

    self.install_license("COPYING")

configure_gen = []
