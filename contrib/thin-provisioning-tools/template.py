pkgname = "thin-provisioning-tools"
pkgver = "1.0.4"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "gmake", "gawk", "pkgconf"]
makedepends = ["rust", "libzstd-devel"]
pkgdesc = "Tools for manipulating the metadata of dm-thin targets"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/jthornber/thin-provisioning-tools"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "a973786fb9cb49d30be6fb8178d6739bc23609d4114ab601f0983ecdbf349abf"
# too long
options = ["!check"]


def do_install(self):
    self.do(
        "gmake",
        "DESTDIR=" + str(self.chroot_destdir),
        "RUST_TARGET=" + self.profile().triplet,
        "install",
    )
