pkgname = "asciidoc"
pkgver = f"9.1.0"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
make_check_target = "test"
hostmakedepends = ["gmake", "python", "docbook-xsl-nons", "xsltproc"]
depends = ["python", "docbook-xsl-nons", "xsltproc"]
pkgdesc = "Text-based document generation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://asciidoc.org"
source = f"https://github.com/asciidoc-py/asciidoc-py/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "fd499fcf51317b1aaf27336fb5e919c44c1f867f1ae6681ee197365d3065238b"
# needs source-highlight, FIXME
options = ["!check"]
