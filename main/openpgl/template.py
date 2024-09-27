pkgname = "openpgl"
pkgver = "0.7.0"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/RenderKit/openpgl"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "58be6ac86e3bcf8a787e9c1332d1527e6d18f4b1403b96bb02c909e20af2ca94"
hardening = ["vis", "cfi"]


@subpackage("openpgl-devel")
def _(self):
    return self.default_devel()
