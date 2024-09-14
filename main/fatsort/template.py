pkgname = "fatsort"
pkgver = "1.6.5.640"
pkgrel = 0
build_style = "makefile"
make_check_target = "tests"
checkdepends = ["bash", "xz"]
pkgdesc = "FAT filesystem sorting utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://fatsort.sourceforge.io"
source = f"$(SOURCEFORGE_SITE)/project/fatsort/fatsort-{pkgver}.tar.xz"
sha256 = "630ece56d9eb3a55524af0aec3aade7854360eba949172a6cfb4768cb8fbe42e"
# a bunch of seemingly locale-related tests fail
options = ["!check"]


def install(self):
    # makefile uses gnu install syntax
    self.install_bin("src/fatsort")
    self.install_man("man/fatsort.1")
