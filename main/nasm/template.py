pkgname = "nasm"
pkgver = "2.16.03"
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
sha256 = "1412a1c760bbd05db026b6c0d1657affd6631cd0a63cddb6f73cc6d4aa616148"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
