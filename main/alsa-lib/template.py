pkgname = "alsa-lib"
pkgver = "1.2.10"
pkgrel = 1
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
sha256 = "c86a45a846331b1b0aa6e6be100be2a7aef92efd405cf6bac7eef8174baa920e"


@subpackage("alsa-lib-devel")
def _devel(self):
    self.depends += ["linux-headers"]
    return self.default_devel()
