pkgname = "liblsdj"
pkgver = "2.2.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
makedepends = ["catch2-devel"]
pkgdesc = "LSDj save format tools"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "MIT"
url = "https://github.com/stijnfrishert/liblsdj"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "74688fca65aa044fb4c8d1211ef013ef7d4fd2ead22b4b075defb0a644e26617"


def check(self):
    self.do("build/liblsdj/test/test")


def post_install(self):
    self.install_license("LICENSE")


@subpackage("liblsdj-devel")
def _(self):
    return self.default_devel()
