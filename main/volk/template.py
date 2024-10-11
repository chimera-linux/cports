pkgname = "volk"
pkgver = "1.3.296.0"
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
sha256 = "8ffd0e81e29688f4abaa39e598937160b098228f37503903b10d481d4862ab85"


def post_install(self):
    self.install_license("LICENSE.md")
