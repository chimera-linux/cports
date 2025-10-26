pkgname = "thin-provisioning-tools"
pkgver = "1.3.0"
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
sha256 = "64b0fcc7960b2ea37a4e5c162aed604337541142c65a5674146b29c706e08671"
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
