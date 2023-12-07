pkgname = "volk"
pkgver = "1.3.270"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DVOLK_INSTALL=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = ["vulkan-headers"]
pkgdesc = "Vulkan meta loader"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/zeux/volk"
source = f"https://github.com/zeux/volk/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "95530bc7850b0358e4bad899eb653f882ee8a08088257d90c5042cec02208f52"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("volk-devel")
def _devel(self):
    return self.default_devel()
