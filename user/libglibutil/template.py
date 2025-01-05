pkgname = "libglibutil"
pkgver = "1.0.79"
pkgrel = 0
build_style = "makefile"
make_install_target = "install-dev"
make_check_target = "test"
make_use_env = True
hostmakedepends = ["pkgconf"]
makedepends = ["glib-devel"]
pkgdesc = "Library of glib utilities"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/sailfishos/libglibutil"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "4d689cb79f8ea061e46b89008370dc771b07164ee496850d9d56d9d85f1be1c3"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libglibutil-devel")
def _(self):
    return self.default_devel()
