pkgname = "nasm"
pkgver = "2.16.01"
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
sha256 = "c77745f4802375efeee2ec5c0ad6b7f037ea9c87c92b149a9637ff099f162558"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")


configure_gen = []
