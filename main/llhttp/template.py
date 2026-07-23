pkgname = "llhttp"
pkgver = "9.4.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "HTTP parser"
license = "MIT"
url = "https://github.com/nodejs/llhttp"
source = f"{url}/archive/release/v{pkgver}.tar.gz"
sha256 = "ba717a2f99f340a0ee9796aaf2b1acca057e1e37682ffd2bc4def4d3b6bc4005"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("llhttp-devel")
def _(self):
    return self.default_devel()
