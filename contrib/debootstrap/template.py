pkgname = "debootstrap"
pkgver = "1.0.137"
pkgrel = 0
build_style = "makefile"
depends = [
    "debian-archive-keyring",
    "cmd:ar!llvm-binutils",
    "cmd:gpgv!gnupg",
    "cmd:mount!mount",
    "cmd:umount!mount",
    "cmd:wget!wget2",
    "cmd:xzcat!xz",
    "cmd:zstdcat!zstd-progs",
]
pkgdesc = "Debian bootstrapping tool"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "MIT"
url = "https://salsa.debian.org/installer-team/debootstrap"
source = f"{url}/-/archive/{pkgver}/debootstrap-{pkgver}.tar.gz"
sha256 = "ddbcacb7b481f91be32c92bae39f2115210b7336d6b9fde51609e628d4f97dd8"
# check: no tests
options = ["!check"]


def post_install(self):
    self.rename("usr/sbin", "bin")
    self.install_license("debian/copyright")
