pkgname = "thin-provisioning-tools"
pkgver = "1.0.13"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable", "gmake", "gawk", "pkgconf"]
makedepends = ["rust-std", "zstd-devel"]
pkgdesc = "Tools for manipulating the metadata of dm-thin targets"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/jthornber/thin-provisioning-tools"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "48444caefd00c23f5240dd01f8b2a51cfded952f078b2a5318929137e00fbd3f"
# too long
options = ["!check"]


def do_install(self):
    self.do(
        "gmake",
        "DESTDIR=" + str(self.chroot_destdir),
        "RUST_TARGET=" + self.profile().triplet,
        "install",
    )
