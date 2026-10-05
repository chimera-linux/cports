pkgname = "llhttp"
pkgver = "9.4.3"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "HTTP parser"
license = "MIT"
url = "https://github.com/nodejs/llhttp"
source = f"{url}/archive/release/v{pkgver}.tar.gz"
sha256 = "1eb813c7437b31a87496a1cd3ed79f00746720f5e7e29c79b42c02cb69f36c39"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("llhttp-devel")
def _(self):
    return self.default_devel()
