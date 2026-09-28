pkgname = "alsa-lib"
pkgver = "1.2.16.1"
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
license = "LGPL-2.1-or-later"
url = "https://www.alsa-project.org"
source = f"{url}/files/pub/lib/alsa-lib-{pkgver}.tar.bz2"
sha256 = "f740db7f488255944ffd4428416ee3390a96742856916433df468c281436480e"


@subpackage("alsa-lib-devel")
def _(self):
    self.depends += ["linux-headers"]
    return self.default_devel()
