pkgname = "rdfind"
pkgver = "1.6.0"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["automake", "libtool", "gmake"]
makedepends = ["nettle-devel"]
pkgdesc = "Duplicate file finder"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://rdfind.pauldreik.se"
source = f"https://rdfind.pauldreik.se/rdfind-{pkgver}.tar.gz"
sha256 = "7a406e8ef1886a5869655604618dd98f672f12c6a6be4926d053be65070f3279"
hardening = ["vis", "cfi"]
# linuxisms in testsuite
options = ["!check"]
