pkgname = "libdbi"
pkgver = "0.9.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
pkgdesc = "Database-independent abstraction layer for C"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "http://libdbi.sourceforge.net"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}/{pkgname}-{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "dafb6cdca524c628df832b6dd0bf8fabceb103248edb21762c02d3068fca4503"


@subpackage("libdbi-devel")
def _devel(self):
    return self.default_devel()


configure_gen = []
