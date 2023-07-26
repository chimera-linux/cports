pkgname = "thin-provisioning-tools"
pkgver = "1.0.5"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo", "gmake", "gawk", "pkgconf"]
makedepends = ["rust", "libzstd-devel"]
pkgdesc = "Tools for manipulating the metadata of dm-thin targets"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/jthornber/thin-provisioning-tools"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "af597c3419ffd10f1d01a36441528565c01a9b88cbca6bee510ab6eeb9086bd1"
# too long
options = ["!check"]


def do_install(self):
    self.do(
        "gmake",
        "DESTDIR=" + str(self.chroot_destdir),
        "RUST_TARGET=" + self.profile().triplet,
        "install",
    )
