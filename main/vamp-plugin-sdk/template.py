pkgname = "vamp-plugin-sdk"
# change source next release (drops .0)
pkgver = "2.10.0"
pkgrel = 1
build_style = "gnu_configure"
make_dir = "."
make_check_target = "test"
hostmakedepends = ["automake", "pkgconf"]
makedepends = ["libsndfile-devel"]
pkgdesc = "Vamp audio analysis plugin system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://www.vamp-plugins.org"
source = "https://github.com/vamp-plugins/vamp-plugin-sdk/archive/refs/tags/vamp-plugin-sdk-v2.10.tar.gz"
sha256 = "b552bc91817294c7f90ea07d70938642ebf15d5e3bafc81cf7d55efab9995399"


def post_install(self):
    self.install_license("COPYING")


@subpackage("vamp-plugin-sdk-devel")
def _(self):
    return self.default_devel()


@subpackage("vamp-plugin-sdk-progs")
def _(self):
    return self.default_progs()
