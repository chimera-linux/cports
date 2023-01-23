pkgname = "cmocka"
pkgver = "1.1.5"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DUNIT_TESTING=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Unit testing framework in C"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://cmocka.org"
source = f"{url}/files/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "f0ccd8242d55e2fd74b16ba518359151f6f8383ff8aef4976e48393f77bba8b6"

@subpackage("cmocka-devel")
def _devel(self):
    return self.default_devel()
