pkgname = "cryptsetup-scripts"
_debver = "4"
_cver = "2.6.1"
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
sha256 = "70ff592c2d0e49cfa18037fb972a47ec0bf28f08eb45559aba78421d623a09b4"
# no test suite
options = ["!check"]
