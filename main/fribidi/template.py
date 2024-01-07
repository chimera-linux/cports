pkgname = "fribidi"
pkgver = "1.0.13"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddocs=false"]
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Free implementation of the Unicode Bidirectional Algorithm"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/fribidi/fribidi"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "f24e8e381bcf76533ae56bd776196f3a0369ec28e9c0fdb6edd163277e008314"
hardening = ["vis", "cfi"]


@subpackage("fribidi-devel")
def _devel(self):
    return self.default_devel()
