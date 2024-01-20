pkgname = "cryptsetup-scripts"
_debver = "6"
_cver = "2.6.1"
pkgver = f"{_cver}.{_debver}"
pkgrel = 1
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
sha256 = "64757be11b49a9ad96f79f81be143792c72f3d6633dd93d654372a62166a9010"
# no test suite
options = ["!check"]
