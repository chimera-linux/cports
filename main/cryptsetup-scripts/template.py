pkgname = "cryptsetup-scripts"
_debver = "1"
_cver = "2.7.1"
pkgver = f"{_cver}.{_debver}"
pkgrel = 0
build_style = "makefile"
make_build_args = [
    "DOCBOOK_XSL=/usr/share/xsl-nons/docbook/manpages/docbook.xsl",
    f"VERSION={pkgver}",
]
hostmakedepends = ["perl", "docbook-xsl-nons", "xsltproc"]
depends = ["cryptsetup", "device-mapper", "mount", "mkfs"]
pkgdesc = "Supporting infrastructure for cryptsetup from Debian"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://salsa.debian.org/cryptsetup-team/cryptsetup"
source = f"{url}/-/archive/debian/2%25{_cver}-{_debver}/cryptsetup-debian-2%25{_cver}-{_debver}.tar.gz"
sha256 = "6340a815e2e2d5e55ec99722e90228b6ff9ab2e4428245bbf3fd4212d161bb29"
# no test suite
options = ["!check"]
