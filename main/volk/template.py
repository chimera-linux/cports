pkgname = "volk"
pkgver = "1.3.295"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/zeux/volk"
source = f"https://github.com/zeux/volk/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "aea9f09c49f8a4e36738003c7aa5f08f99d68b96e4028ad9fa9039d2ee9fb251"


def post_install(self):
    self.install_license("LICENSE.md")
