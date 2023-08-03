pkgname = "docbook-xml"
pkgver = "4.5"
pkgrel = 0
depends = ["xmlcatmgr"]
pkgdesc = "XML DTD designed for computer documentation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://www.oasis-open.org/docbook"
source = [
    f"http://www.oasis-open.org/docbook/xml/{pkgver}/docbook-xml-{pkgver}.zip",
    "http://www.oasis-open.org/docbook/xml/4.4/docbook-xml-4.4.zip",
    "http://www.oasis-open.org/docbook/xml/4.3/docbook-xml-4.3.zip",
    "http://www.oasis-open.org/docbook/xml/4.2/docbook-xml-4.2.zip",
]
sha256 = [
    "4e4e037a2b83c98c6c94818390d4bdd3f6e10f6ec62dd79188594e26190dc7b4",
    "02f159eb88c4254d95e831c51c144b1863b216d909b5ff45743a1ce6f5273090",
    "23068a94ea6fd484b004c5a73ec36a66aa47ea8f0d6b62cc1695931f5c143464",
    "acc4601e4f97a196076b7e64b368d9248b07c7abf26b34a02cca40eeebe60fa2",
]
_url = "http://www.oasis-open.org/docbook/xml"
_path = "/usr/share/xml/docbook"
xml_entries = [
    ("rewriteSystem", f"{_url}/4.2", f"{_path}/4.2"),
    ("rewriteSystem", f"{_url}/4.3", f"{_path}/4.3"),
    ("rewriteSystem", f"{_url}/4.4", f"{_path}/4.4"),
    ("rewriteSystem", f"{_url}/4.5", f"{_path}/4.5"),
    ("rewriteSystem", f"{_url}/4.1.2", f"{_path}/4.2"),
]
xml_catalogs = [
    f"{_path}/4.2/catalog",
    f"{_path}/4.3/catalog",
    f"{_path}/4.4/catalog",
    f"{_path}/4.5/catalog",
    f"{_path}/4.2/catalog-4.1.2",
]


def do_extract(self):
    pass


def do_install(self):
    vers = ["4.2", "4.3", "4.4", "4.5"]

    for v in vers:
        tdir = f"usr/share/xml/docbook/{v}"
        fname = f"{pkgname}-{v}.zip"
        self.install_dir(tdir)
        self.cp(self.sources_path / fname, self.destdir / tdir)
        self.do(
            "tar",
            "xf",
            self.chroot_destdir / tdir / fname,
            "-C",
            self.chroot_destdir / tdir,
            "--uid",
            "0",
            "--gid",
            "0",
        )
        self.rm(self.destdir / tdir / fname)
        self.mv(
            self.destdir / tdir / "catalog.xml", self.destdir / tdir / "catalog"
        )

    with self.pushd(self.destdir / "usr/share/xml/docbook/4.2"):
        with open(self.cwd / "catalog-4.1.2", "w") as ocat:
            with open(self.cwd / "catalog") as icat:
                for ln in icat:
                    ocat.write(ln.replace("V4.2", "V4.1.2"))
