pkgname = "thin-provisioning-tools"
pkgver = "1.1.0"
pkgrel = 1
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/jthornber/thin-provisioning-tools"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "fef778119046e6057aabcc087685aafefe62eb3a65febba639482e72c85a59ed"
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
