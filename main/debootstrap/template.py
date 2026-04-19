pkgname = "debootstrap"
pkgver = "1.0.143"
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
sha256 = "15652a91eb1cf04c24c485bbaaf36e0528132bded8475820344a8129c7eaca01"
# check: no tests
options = ["!check"]


def post_install(self):
    self.rename("usr/sbin", "bin")
    self.install_license("debian/copyright")
