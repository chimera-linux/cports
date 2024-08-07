pkgname = "debootstrap"
pkgver = "1.0.137"
pkgrel = 0
build_style = "makefile"
depends = [
    "debian-archive-keyring",
    "virtual:cmd:ar!llvm-binutils",
    "virtual:cmd:gpgv!gnupg",
    "virtual:cmd:mount!mount",
    "virtual:cmd:umount!mount",
    "virtual:cmd:wget!wget2",
    "virtual:cmd:xzcat!xz",
    "virtual:cmd:zstdcat!zstd-progs",
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
