pkgname = "debootstrap"
pkgver = "1.0.139"
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
sha256 = "098fba8a4e751da993db3c3db49934279336ac4b635e3647de33fe7eb3de42ed"
# check: no tests
options = ["!check"]


def post_install(self):
    self.rename("usr/sbin", "bin")
    self.install_license("debian/copyright")
