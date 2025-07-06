pkgname = "libglibutil"
pkgver = "1.0.80"
pkgrel = 0
build_style = "makefile"
make_install_target = "install-dev"
make_check_target = "test"
make_use_env = True
hostmakedepends = ["pkgconf"]
makedepends = ["glib-devel"]
pkgdesc = "Library of glib utilities"
license = "BSD-3-Clause"
url = "https://github.com/sailfishos/libglibutil"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "ab4728157b68f84492512c7a451fe193924ae2aac3aa851de06eb3fd5acdc714"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libglibutil-devel")
def _(self):
    return self.default_devel()
