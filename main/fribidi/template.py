pkgname = "fribidi"
pkgver = "1.0.12"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddocs=false"]
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Free implementation of the Unicode Bidirectional Algorithm"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/fribidi/fribidi"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "2e9e859876571f03567ac91e5ed3b5308791f31cda083408c2b60fa1fe00a39d"
hardening = ["vis", "cfi"]


@subpackage("fribidi-devel")
def _devel(self):
    return self.default_devel()
