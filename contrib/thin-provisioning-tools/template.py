pkgname = "thin-provisioning-tools"
pkgver = "1.0.10"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "gmake", "gawk", "pkgconf"]
makedepends = ["rust-std", "zstd-devel"]
pkgdesc = "Tools for manipulating the metadata of dm-thin targets"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/jthornber/thin-provisioning-tools"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "2cd25a6e7d0afd2cff25a392a37f94b13dadc51d7c3962c91f7f9762098b0842"
# too long
options = ["!check"]


def do_install(self):
    self.do(
        "gmake",
        "DESTDIR=" + str(self.chroot_destdir),
        "RUST_TARGET=" + self.profile().triplet,
        "install",
    )
