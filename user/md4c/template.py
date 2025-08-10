pkgname = "md4c"
pkgver = "0.5.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Fast CommonMark compliant markdown parser"
license = "MIT"
url = "https://github.com/mity/md4c"
source = f"{url}/archive/release-{pkgver}.tar.gz"
sha256 = "55d0111d48fb11883aaee91465e642b8b640775a4d6993c2d0e7a8092758ef21"


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("md4c-devel")
def _(self):
    return self.default_devel()
