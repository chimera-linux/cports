pkgname = "liblc3"
pkgver = "1.1.2"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dtools=true"]
hostmakedepends = ["meson", "pkgconf"]
pkgdesc = "Low complexity communicationcodec"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/google/liblc3"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "6903e2ea3221fcd55d03b9ab390a7921f7ef2147a3934155690664b30d6ff9ec"


@subpackage("liblc3-devel")
def _(self):
    return self.default_devel()
