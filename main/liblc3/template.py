pkgname = "liblc3"
pkgver = "1.0.4"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dtools=true"]
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Low complexity communicationcodec"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/google/liblc3"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "9cf7177b864cac7612f27c0737440b1b7b53d88687778405060de29dfd6e0aaa"


@subpackage("liblc3-devel")
def _devel(self):
    return self.default_devel()
