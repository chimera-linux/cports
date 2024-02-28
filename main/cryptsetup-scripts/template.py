pkgname = "cryptsetup-scripts"
_debver = "1"
_cver = "2.7.0"
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
sha256 = "9cd6cf4bf5a1a85ed66852df0e53ba540ec832f6d3d97dcd90fa6dc28c172bda"
# no test suite
options = ["!check"]
