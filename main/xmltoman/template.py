pkgname = "xmltoman"
pkgver = "0.4"
pkgrel = 1
build_style = "makefile"
make_cmd = "gmake"
hostmakedepends = ["gmake", "perl", "perl-xml-parser"]
depends = ["perl", "perl-xml-parser"]
pkgdesc = "Convert XML to manpages in groff format or HTML"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://sourceforge.net/projects/xmltoman"
source = f"https://github.com/Distrotech/xmltoman/archive/{pkgver}.tar.gz"
sha256 = "2ab86b74fe364a866d84c14b20cbd42a09fa85c629deeff52376bbf890854feb"
hardening = ["vis", "cfi"]
# no test suite
options = ["!check"]
