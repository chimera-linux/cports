pkgname = "libgrapheme"
pkgver = "2.0.2"
pkgrel = 1
build_style = "makefile"
make_check_target = "test"
hostmakedepends = ["pkgconf"]
pkgdesc = "Unicode string library"
maintainer = "ttyyls <contact@behri.org>"
license = "ISC AND Unicode-3.0"
url = "https://libs.suckless.org/libgrapheme"
source = f"https://dl.suckless.org/libgrapheme/libgrapheme-{pkgver}.tar.gz"
sha256 = "a68bbddde76bd55ba5d64116ce5e42a13df045c81c0852de9ab60896aa143125"
# link errors on ppc*
options = ["!lto"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_license("data/LICENSE", name="LICENSE-UNICODE")


@subpackage("libgrapheme-devel")
def _(self):
    return self.default_devel()
