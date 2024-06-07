pkgname = "volk"
pkgver = "1.3.283.0"
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
source = (
    f"https://github.com/zeux/volk/archive/refs/tags/vulkan-sdk-{pkgver}.tar.gz"
)
sha256 = "872035f1f26c53b218632a3a8dbccbd276710aaabafb9bb1bc1a6c0633ee6aab"


def post_install(self):
    self.install_license("LICENSE.md")
