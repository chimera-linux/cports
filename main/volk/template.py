pkgname = "volk"
pkgver = "1.4.357.0"
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
license = "MIT"
url = "https://github.com/zeux/volk"
source = (
    f"https://github.com/zeux/volk/archive/refs/tags/vulkan-sdk-{pkgver}.tar.gz"
)
sha256 = "6400c7b23e24d17e4f04bac49b55b06c4e87677d33398e90344743ec73560ca6"


def post_install(self):
    self.install_license("LICENSE.md")
