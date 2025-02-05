pkgname = "debootstrap"
pkgver = "1.0.140"
pkgrel = 0
build_style = "makefile"
depends = [
    "debian-archive-keyring",
    "cmd:ar!llvm-binutils",
    "cmd:gpgv!gnupg",
    "cmd:mount!util-linux-mount",
    "cmd:umount!util-linux-mount",
    "cmd:wget!wget2",
    "cmd:xzcat!xz",
    "cmd:zstdcat!zstd-progs",
]
pkgdesc = "Debian bootstrapping tool"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "MIT"
url = "https://salsa.debian.org/installer-team/debootstrap"
source = f"{url}/-/archive/{pkgver}/debootstrap-{pkgver}.tar.gz"
sha256 = "6bf6ec0e40ab683b1cb532089e3646a440c7a5273146295aaf4df87963dc0784"
# check: no tests
options = ["!check"]


def post_install(self):
    self.rename("usr/sbin", "bin")
    self.install_license("debian/copyright")
