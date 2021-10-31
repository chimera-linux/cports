pkgname = "docbook-xsl"
pkgver = f"1.79.2"
pkgrel = 0
depends = ["xmlcatmgr", "docbook-xml"]
pkgdesc = "Docbook XSL modular stylesheet"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://docbook.org"
source = f"https://github.com/docbook/xslt10-stylesheets/releases/download/release/{pkgver}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "316524ea444e53208a2fb90eeb676af755da96e1417835ba5f5eb719c81fa371"

def do_install(self):
    self.install_license("COPYING")

    self.install_file("catalog.xml", "usr/share/xsl-ns/docbook")
    self.install_file("VERSION", "usr/share/xsl-ns/docbook")
    self.install_file("VERSION.xsl", "usr/share/xsl-ns/docbook")

    for d in [
        "assembly", "common", "eclipse", "epub", "epub3", "fo",
        "highlighting", "html", "htmlhelp", "images", "javahelp", "lib",
        "manpages", "params", "profiling", "roundtrip", "template",
        "slides", "website", "xhtml", "xhtml-1_1", "xhtml5"
    ]:
        self.install_dir(f"usr/share/xsl-ns/docbook/{d}")
        for f in (self.cwd / d).glob("*"):
            self.cp(
                f, self.destdir / f"usr/share/xsl-ns/docbook/{d}",
                recursive = True
            )
