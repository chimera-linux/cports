pkgname = "openpgl"
pkgver = "0.7.1"
pkgrel = 0
# others unsupported
archs = ["aarch64", "x86_64"]
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = ["onetbb-devel"]
pkgdesc = "Intel path guiding library"
license = "Apache-2.0"
url = "https://github.com/RenderKit/openpgl"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d62d24241232a526491328f341df9add274fc84ae9818470d3edb5ae6141ac63"
hardening = ["vis", "cfi"]


@subpackage("openpgl-devel")
def _(self):
    return self.default_devel()
