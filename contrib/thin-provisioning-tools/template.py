pkgname = "thin-provisioning-tools"
pkgver = "1.0.3"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "gmake", "gawk"]
makedepends = ["rust"]
pkgdesc = "Tools for manipulating the metadata of dm-thin targets"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/jthornber/thin-provisioning-tools"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "8c912be0f7a1cdc40f37fd4226a1794a91fa31667231d4e88338f32cf84b88b6"
# too long
options = ["!check"]


def do_install(self):
    self.do(
        "gmake",
        "DESTDIR=" + str(self.chroot_destdir),
        "RUST_TARGET=" + self.profile().triplet,
        "install",
    )
