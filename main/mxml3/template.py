# 4.x is not compatible with most stuff yet (and is named mxml4 in .pc)
pkgname = "mxml3"
pkgver = "3.3.1"
pkgrel = 0
build_style = "gnu_configure"
# fails reconf
configure_gen = []
make_dir = "."
make_check_target = "test"
hostmakedepends = ["automake", "pkgconf"]
pkgdesc = "C XML Library"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://www.msweet.org/mxml"
source = f"https://github.com/michaelrsweet/mxml/archive/v{pkgver}.tar.gz"
sha256 = "59eba16ce43765f2e2a6cf4873a58d317be801f1e929647d85da9f171e41e9ac"


def init_install(self):
    self.make_install_args += [f"BUILDROOT={self.chroot_destdir}"]


@subpackage("mxml3-devel")
def _(self):
    return self.default_devel()
