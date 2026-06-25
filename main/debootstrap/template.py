pkgname = "debootstrap"
pkgver = "1.0.144"
pkgrel = 0
build_style = "makefile"
depends = [
    "cmd:ar!llvm-binutils",
    "cmd:gpgv!gnupg",
    "cmd:mount!util-linux-mount",
    "cmd:umount!util-linux-mount",
    "cmd:wget!wget2",
    "cmd:xzcat!xz",
    "cmd:zstdcat!zstd-progs",
    "debian-archive-keyring",
]
pkgdesc = "Debian bootstrapping tool"
license = "MIT"
url = "https://salsa.debian.org/installer-team/debootstrap"
source = f"{url}/-/archive/{pkgver}/debootstrap-{pkgver}.tar.gz"
sha256 = "a35b2180d48d981a6db8602706bd229e65514503768933c0f797c66927c76631"
# check: no tests
options = ["!check"]


def post_install(self):
    self.rename("usr/sbin", "bin")
    self.install_license("debian/copyright")
