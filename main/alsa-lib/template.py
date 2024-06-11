pkgname = "alsa-lib"
pkgver = "1.2.12"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-alisp",
    "--disable-old-symbols",
    "--disable-python",
    "--with-versioned=no",
]
hostmakedepends = ["pkgconf", "automake", "libtool"]
makedepends = ["linux-headers"]
depends = ["alsa-ucm-conf"]
pkgdesc = "Advanced Linux Sound Architecture library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://www.alsa-project.org"
source = f"{url}/files/pub/lib/{pkgname}-{pkgver}.tar.bz2"
sha256 = "4868cd908627279da5a634f468701625be8cc251d84262c7e5b6a218391ad0d2"


@subpackage("alsa-lib-devel")
def _devel(self):
    self.depends += ["linux-headers"]
    return self.default_devel()
