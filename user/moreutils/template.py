pkgname = "moreutils"
pkgver = "0.70"
pkgrel = 0
build_style = "makefile"
make_build_args = ["DOCBOOKXSL=/usr/share/xsl-nons/docbook"]
hostmakedepends = [
    "docbook-xsl-nons",
    "libxml2-progs",
    "perl",
    "libxslt-progs",
]
makedepends = ["linux-headers"]
depends = ["perl-ipc-run"]
pkgdesc = "Miscallaenous unix utilities"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-2.0-or-later"
url = "https://joeyh.name/code/moreutils"
source = f"https://git.joeyh.name/index.cgi/moreutils.git/snapshot/moreutils-{pkgver}.tar.gz"
sha256 = "f2bf46d410ba567cc8d01507e94916994e48742722e690dc498fab59f5250132"
hardening = ["vis", "cfi"]
# no tests defined
options = ["!check"]
