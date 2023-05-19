pkgname = "vamp-plugin-sdk"
pkgver = "2.10.0"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
make_check_target = "test"
hostmakedepends = ["pkgconf", "gmake"]
makedepends = ["libsndfile-devel"]
pkgdesc = "Vamp audio analysis plugin system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.vamp-plugins.org"
source = f"https://code.soundsoftware.ac.uk/attachments/download/2691/{pkgname}-{pkgver}.tar.gz"
sha256 = "aeaf3762a44b148cebb10cde82f577317ffc9df2720e5445c3df85f3739ff75f"
# fails to link
options = ["!lto"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("vamp-plugin-sdk-devel")
def _devel(self):
    return self.default_devel()

@subpackage("vamp-plugin-sdk-progs")
def _xmlwf(self):
    return self.default_progs()

configure_gen = []
