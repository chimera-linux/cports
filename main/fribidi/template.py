pkgname = "fribidi"
pkgver = "1.0.16"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddocs=false"]
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Free implementation of the Unicode Bidirectional Algorithm"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/fribidi/fribidi"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "5a1d187a33daa58fcee2ad77f0eb9d136dd6fa4096239199ba31e850d397e8a8"
hardening = ["vis", "cfi"]


@subpackage("fribidi-devel")
def _(self):
    return self.default_devel()
