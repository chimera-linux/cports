pkgname = "liblc3"
pkgver = "1.1.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dtools=true"]
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Low complexity communicationcodec"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/google/liblc3"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "b65e38943708529efd04a87dd1a9f16a9856ed6199d082b18e7d42fb5c59486e"


@subpackage("liblc3-devel")
def _devel(self):
    return self.default_devel()
