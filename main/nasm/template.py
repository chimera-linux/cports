pkgname = "nasm"
pkgver = "2.15.05"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
make_check_target = "test"
hostmakedepends = ["gmake"]
checkdepends = ["perl"]
pkgdesc = "80x86 assembler designed for portability and modularity"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://www.nasm.us"
source = f"{url}/pub/{pkgname}/releasebuilds/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "3caf6729c1073bf96629b57cee31eeb54f4f8129b01902c73428836550b30a3f"

def post_install(self):
    self.install_license("LICENSE")
