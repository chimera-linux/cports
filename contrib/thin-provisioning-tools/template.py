pkgname = "thin-provisioning-tools"
pkgver = "1.0.9"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "gmake", "gawk", "pkgconf"]
makedepends = ["rust-std", "zstd-devel"]
pkgdesc = "Tools for manipulating the metadata of dm-thin targets"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/jthornber/thin-provisioning-tools"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "830a6f86f96bfaadd779ca36b15a02b21fd1082ea0e72102b269d999d0b20429"
# too long
options = ["!check"]


def do_install(self):
    self.do(
        "gmake",
        "DESTDIR=" + str(self.chroot_destdir),
        "RUST_TARGET=" + self.profile().triplet,
        "install",
    )
