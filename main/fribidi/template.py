pkgname = "fribidi"
pkgver = "1.0.11"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddocs=false"]
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Free implementation of the Unicode Bidirectional Algorithm"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/fribidi/fribidi"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "0e6d631c184e1012fb3ae86e80adabf26e46b4ffee2332e679eb308edd337398"

@subpackage("fribidi-static")
def _static(self):
    return self.default_static()

@subpackage("fribidi-devel")
def _devel(self):
    return self.default_devel()
