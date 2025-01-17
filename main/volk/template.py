pkgname = "volk"
pkgver = "1.4.304"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DVOLK_HEADERS_ONLY=ON",
    "-DVOLK_INSTALL=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = ["vulkan-headers"]
pkgdesc = "Vulkan meta loader"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/zeux/volk"
source = f"https://github.com/zeux/volk/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "ab3d4a8ccaeb32652259cdd008399504a41792675b0421d90b67729ee274746f"


def post_install(self):
    self.install_license("LICENSE.md")
