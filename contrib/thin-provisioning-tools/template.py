pkgname = "thin-provisioning-tools"
pkgver = "1.0.14"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "gawk",
    "gmake",
    "pkgconf",
]
makedepends = [
    "device-mapper-devel",
    "linux-headers",
    "rust-std",
    "udev-devel",
    "zstd-devel",
]
pkgdesc = "Tools for manipulating the metadata of dm-thin targets"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/jthornber/thin-provisioning-tools"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "5abe8a23b077596dc9134396aa4bd0a288bf6fd63d455715d5a41a325b3ec2e6"
# too long
options = ["!check"]


def do_install(self):
    self.do(
        "gmake",
        "DESTDIR=" + str(self.chroot_destdir),
        "RUST_TARGET=" + self.profile().triplet,
        "install",
    )
