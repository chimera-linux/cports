pkgname = "asciidoc"
pkgver = "10.2.1"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "docbook-xsl-nons",
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
    "libxslt-progs",
]
depends = ["python", "docbook-xsl-nons", "libxslt-progs", "libxml2-progs"]
pkgdesc = "Text-based document generation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://asciidoc.org"
source = f"$(PYPI_SITE)/a/asciidoc/asciidoc-{pkgver}.tar.gz"
sha256 = "d9f13c285981b3c7eb660d02ca0a2779981e88d48105de81bb40445e60dddb83"
# apparently only supports tox now and that's useless
options = ["!check"]


def post_install(self):
    self.install_dir("etc")
    # compat link
    for f in (self.destdir / "usr/lib").glob("python*"):
        adpath = f / "site-packages/asciidoc/resources"
        self.install_link(
            "etc/asciidoc", f"../{adpath.relative_to(self.destdir)}"
        )
