pkgname = "vulkan-utility-libraries"
pkgver = "1.3.288"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_TESTS=ON"]
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = [
    "gtest-devel",
    "magic_enum",
    "vulkan-headers",
]
depends = ["vulkan-headers"]
pkgdesc = "Utility libraries for Vulkan"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/KhronosGroup/Vulkan-Utility-Libraries"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9192bd1352162d524b80d1d5edb5752eb3c9ba15c053a0f2b51b63e461a6c0a5"
# static-only library, so just keep it as one package
options = ["!lintstatic"]
