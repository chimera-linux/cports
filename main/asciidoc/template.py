pkgname = "asciidoc"
pkgver = "10.2.0"
pkgrel = 2
build_style = "python_pep517"
hostmakedepends = [
    "docbook-xsl-nons",
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
    "xsltproc",
]
depends = ["python", "docbook-xsl-nons", "xsltproc", "libxml2-progs"]
pkgdesc = "Text-based document generation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://asciidoc.org"
source = f"$(PYPI_SITE)/a/asciidoc/asciidoc-{pkgver}.tar.gz"
sha256 = "91ff1dd4c85af7b235d03e0860f0c4e79dd1ff580fb610668a39b5c77b4ccace"
# apparently only supports tox now and that's useless
options = ["!check"]


def post_install(self):
    self.install_dir("etc")
    # compat link
    for f in (self.destdir / "usr/lib").glob("python*"):
        adpath = f / "site-packages/asciidoc/resources"
        self.install_link(
            f"../{adpath.relative_to(self.destdir)}", "etc/asciidoc"
        )
