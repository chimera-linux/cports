pkgname = "exfatprogs"
pkgver = "1.2.1"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = [
    "automake",
    "autoconf",
    "gmake",
    "libtool",
    "linux-headers",
]
makedepends = []
pkgdesc = "ExFAT filesystem utilities"
maintainer = "Val Packett <val@packett.cool>"
license = "MIT"
url = "https://github.com/exfatprogs/exfatprogs"
source = f"{url}/releases/download/{pkgver}/exfatprogs-{pkgver}.tar.xz"
sha256 = "a6f3b1fb4bd37835c8f8cb421aac4eb75b880a51342b29850c4063973162227b"


def post_install(self):
    self.install_license("COPYING")
