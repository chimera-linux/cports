pkgname = "musl-nscd"
pkgver = "1.1.1"
pkgrel = 5
build_style = "gnu_configure"
configure_env = {"YACC": "bison"}
configure_gen = []
make_dir = "."
hostmakedepends = ["flex", "bison"]
pkgdesc = "NSS to NSCD bridge for musl"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/pikhq/musl-nscd"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "ddd5924f0355568a483cb8c83e63c7e3425b8c3f1dce4b9883ca75ed1a276675"
hardening = ["vis", "cfi"]
# no test suite
options = ["!check"]


def post_install(self):
    self.install_license("COPYRIGHT")
    self.install_tmpfiles(self.files_path / "nscd.conf")
    self.install_service(self.files_path / "nscd")
