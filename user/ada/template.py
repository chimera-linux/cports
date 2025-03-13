pkgname = "ada"
pkgver = "3.2.1"
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
sha256 = "2530b601224d96554333ef2e1504cebf040e86b79a4166616044f5f79c47eaa5"


def post_install(self):
    self.install_license("LICENSE-MIT")


@subpackage("ada-devel")
def _(self):
    return self.default_devel()
