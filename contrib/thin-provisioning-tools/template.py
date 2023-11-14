pkgname = "thin-provisioning-tools"
pkgver = "1.0.7"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "gmake", "gawk", "pkgconf"]
makedepends = ["rust-std", "zstd-devel"]
pkgdesc = "Tools for manipulating the metadata of dm-thin targets"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/jthornber/thin-provisioning-tools"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "6fd53f6c9aa70dc43b808858f3bd5b1c49279b8773bcd5c750ae21903559e629"
# too long
options = ["!check"]


def do_install(self):
    self.do(
        "gmake",
        "DESTDIR=" + str(self.chroot_destdir),
        "RUST_TARGET=" + self.profile().triplet,
        "install",
    )
