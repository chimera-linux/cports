pkgname = "alsa-lib"
pkgver = "1.2.14"
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
license = "LGPL-2.1-or-later"
url = "https://www.alsa-project.org"
source = f"{url}/files/pub/lib/alsa-lib-{pkgver}.tar.bz2"
sha256 = "be9c88a0b3604367dd74167a2b754a35e142f670292ae47a2fdef27a2ee97a32"


@subpackage("alsa-lib-devel")
def _(self):
    self.depends += ["linux-headers"]
    return self.default_devel()
