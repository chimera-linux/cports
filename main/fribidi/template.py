pkgname = "fribidi"
pkgver = "1.0.14"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddocs=false"]
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Free implementation of the Unicode Bidirectional Algorithm"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/fribidi/fribidi"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "7b1b3837f6583432068c71ca333a8988c803e9b94259edbd37c85367bbc51446"
hardening = ["vis", "cfi"]


@subpackage("fribidi-devel")
def _devel(self):
    return self.default_devel()
