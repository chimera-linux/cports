pkgname = "debootstrap"
pkgver = "1.0.138"
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
sha256 = "1a3db9f6d198507fb8e7b8eb38b08d4e7b80a929ec5f3e36531c7b7acfcdc0dc"
# check: no tests
options = ["!check"]


def post_install(self):
    self.rename("usr/sbin", "bin")
    self.install_license("debian/copyright")
