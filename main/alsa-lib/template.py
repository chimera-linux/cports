pkgname = "alsa-lib"
pkgver = "1.2.13"
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
source = f"{url}/files/pub/lib/alsa-lib-{pkgver}.tar.bz2"
sha256 = "8c4ff37553cbe89618e187e4c779f71a9bb2a8b27b91f87ed40987cc9233d8f6"


@subpackage("alsa-lib-devel")
def _(self):
    self.depends += ["linux-headers"]
    return self.default_devel()
