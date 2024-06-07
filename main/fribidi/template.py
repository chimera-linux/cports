pkgname = "fribidi"
pkgver = "1.0.15"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddocs=false"]
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Free implementation of the Unicode Bidirectional Algorithm"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/fribidi/fribidi"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "0db5f0621b6fbfae5960c30da4f132009fd72bf4687f1b04a87a4cfc2a08ea38"
hardening = ["vis", "cfi"]


@subpackage("fribidi-devel")
def _devel(self):
    return self.default_devel()
