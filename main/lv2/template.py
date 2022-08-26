pkgname = "lv2"
pkgver = "1.18.8"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["libsndfile-devel"]
pkgdesc = "Plugin standard for audio systems"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC"
url = "https://lv2plug.in"
source = f"{url}/spec/{pkgname}-{pkgver}.tar.xz"
sha256 = "b404cf14f776af40ca43808b45f4219dfa850a4f47aa33f89fa96ae719e174c8"

def post_install(self):
    self.install_license("COPYING")
