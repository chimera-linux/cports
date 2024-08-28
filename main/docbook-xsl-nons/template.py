pkgname = "docbook-xsl-nons"
pkgver = "1.79.2"
pkgrel = 1
depends = ["xmlcatmgr", "docbook-xml"]
pkgdesc = "Docbook XSL modular stylesheet"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://docbook.org"
source = f"https://github.com/docbook/xslt10-stylesheets/releases/download/release/{pkgver}/docbook-xsl-nons-{pkgver}.tar.bz2"
sha256 = "ee8b9eca0b7a8f89075832a2da7534bce8c5478fc8fc2676f512d5d87d832102"


def install(self):
    self.install_license("COPYING")

    self.install_file(
        self.files_path / "docbook-xsl-nons.conf", "usr/share/xml/catalogs"
    )

    self.install_file("catalog.xml", "usr/share/xsl-nons/docbook")
    self.install_file("VERSION", "usr/share/xsl-nons/docbook")
    self.install_file("VERSION.xsl", "usr/share/xsl-nons/docbook")

    for d in [
        "assembly",
        "common",
        "eclipse",
        "epub",
        "epub3",
        "fo",
        "highlighting",
        "html",
        "htmlhelp",
        "images",
        "javahelp",
        "lib",
        "manpages",
        "params",
        "profiling",
        "roundtrip",
        "template",
        "slides",
        "website",
        "xhtml",
        "xhtml-1_1",
        "xhtml5",
    ]:
        self.install_dir(f"usr/share/xsl-nons/docbook/{d}")
        for f in (self.cwd / d).glob("*"):
            self.cp(
                f,
                self.destdir / f"usr/share/xsl-nons/docbook/{d}",
                recursive=True,
            )
