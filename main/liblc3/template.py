pkgname = "liblc3"
pkgver = "1.1.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dtools=true"]
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Low complexity communicationcodec"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/google/liblc3"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "958725e277685f9506d30ea341c38a03b245c3b33852cd074da6c8857525e808"


@subpackage("liblc3-devel")
def _devel(self):
    return self.default_devel()
