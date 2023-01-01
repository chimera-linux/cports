pkgname = "cryptsetup-scripts"
_debver = "6"
_cver = "2.5.0"
pkgver = f"{_cver}.{_debver}"
pkgrel = 0
build_style = "makefile"
make_build_args = [
    "DOCBOOK_XSL=/usr/share/xsl-nons/docbook/manpages/docbook.xsl",
    f"VERSION={pkgver}"
]
hostmakedepends = ["perl", "docbook-xsl-nons", "xsltproc"]
depends = ["cryptsetup", "util-linux"]
pkgdesc = "Supporting infrastructure for cryptsetup from Debian"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://salsa.debian.org/cryptsetup-team/cryptsetup"
source = f"{url}/-/archive/debian/2%25{_cver}-{_debver}/cryptsetup-debian-2%25{_cver}-{_debver}.tar.gz"
sha256 = "e9c53c79347ee597b8218d7ec505ae5b6175e9fbe9f27c11945da30b1a00a3cc"
# no test suite
options = ["!check"]
