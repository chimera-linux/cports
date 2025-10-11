pkgname = "thin-provisioning-tools"
pkgver = "1.2.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "gawk",
    "pkgconf",
]
makedepends = [
    "linux-headers",
    "lvm2-devel",
    "rust-std",
    "udev-devel",
    "zstd-devel",
]
pkgdesc = "Tools for manipulating the metadata of dm-thin targets"
license = "GPL-3.0-or-later"
url = "https://github.com/jthornber/thin-provisioning-tools"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "8ac15a068e6a6aec0cf0343d3d76f88c397d5fb2d6bd6202e9f13a490a9f3e22"
# too long
options = ["!check"]

if self.profile().wordsize == 32:
    broken = "needs atomic64"


def install(self):
    self.do(
        "make",
        "DESTDIR=" + str(self.chroot_destdir),
        "RUST_TARGET=" + self.profile().triplet,
        "install",
    )
