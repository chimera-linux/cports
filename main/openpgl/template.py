pkgname = "openpgl"
pkgver = "0.6.0"
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
sha256 = "4192a4096ee3e3d31878cd013f8de23418c8037c576537551f946c4811931c5e"
hardening = ["vis", "cfi"]


@subpackage("openpgl-devel")
def _(self):
    return self.default_devel()
