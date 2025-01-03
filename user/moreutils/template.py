pkgname = "moreutils"
pkgver = "0.69"
pkgrel = 0
build_style = "makefile"
make_build_args = ["DOCBOOKXSL=/usr/share/xsl-nons/docbook"]
hostmakedepends = [
    "docbook-xsl-nons",
    "libxml2-progs",
    "perl",
    "xsltproc",
]
makedepends = ["linux-headers"]
pkgdesc = "Miscallaenous unix utilities"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-2.0-or-later"
url = "https://joeyh.name/code/moreutils"
source = f"http://deb.debian.org/debian/pool/main/m/moreutils/moreutils_{pkgver}.orig.tar.xz"
sha256 = "2170c46219ce8d6f17702321534769dfbfece52148a78cd12ea73b5d3a72ff7c"
hardening = ["vis", "cfi"]
# no tests defined
options = ["!check"]
