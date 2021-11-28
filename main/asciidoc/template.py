pkgname = "asciidoc"
pkgver = "10.0.2"
pkgrel = 0
build_style = "python_module"
hostmakedepends = ["python-setuptools", "docbook-xsl-nons", "xsltproc"]
depends = ["python", "docbook-xsl-nons", "xsltproc"]
pkgdesc = "Text-based document generation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://asciidoc.org"
source = f"$(PYPI_SITE)/a/asciidoc/asciidoc-{pkgver}.tar.gz"
sha256 = "1800699c579038bcf68e760e9358304b69a19ef04c9bf0b4faa76b729dcf7dbf"
# needs source-highlight, FIXME
options = ["!check", "lto"]
