pkgname = "lv2"
pkgver = "1.18.2"
pkgrel = 0
build_style = "waf"
hostmakedepends = ["python", "pkgconf"]
makedepends = ["libsndfile-devel"]
pkgdesc = "Plugin standard for audio systems"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC"
url = "https://lv2plug.in"
source = f"{url}/spec/{pkgname}-{pkgver}.tar.bz2"
sha256 = "4e891fbc744c05855beb5dfa82e822b14917dd66e98f82b8230dbd1c7ab2e05e"
# FIXME check
options = ["!cross", "!check"]

def post_install(self):
    self.install_license("COPYING")
