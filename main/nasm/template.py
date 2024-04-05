pkgname = "nasm"
pkgver = "2.16.02"
pkgrel = 0
build_style = "gnu_configure"
# fails to regen
configure_gen = []
make_cmd = "gmake"
make_dir = "."
make_check_target = "test"
hostmakedepends = ["asciidoc", "gmake"]
checkdepends = ["perl"]
pkgdesc = "80x86 assembler designed for portability and modularity"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://www.nasm.us"
source = f"{url}/pub/{pkgname}/releasebuilds/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "1e1b942ea88f22edae89659e15be26fa027eae0747f51413540f52d4eac4790d"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
