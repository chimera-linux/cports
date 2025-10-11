pkgname = "ada"
pkgver = "3.3.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    # these want cpm
    "-DADA_BENCHMARKS=OFF",
    "-DADA_TESTING=OFF",
    "-DADA_TOOLS=OFF",
    "-DBUILD_SHARED_LIBS=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "URL parser library"
license = "MIT OR Apache-2.0"
url = "https://www.ada-url.com"
source = f"https://github.com/ada-url/ada/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "75565e2d4cc8e3ce2dd7927f5c75cc5ebbd3b620468cb0226501dae68d8fe1cd"


def post_install(self):
    self.install_license("LICENSE-MIT")


@subpackage("ada-devel")
def _(self):
    return self.default_devel()
