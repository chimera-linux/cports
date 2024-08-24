pkgname = "vulkan-utility-libraries"
pkgver = "1.3.294"
pkgrel = 1
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
sha256 = "9b008530f9ddf9ce05e0fb7adaf8ebb7517a5816c969ace592b3756fdaa8ec97"
# static-only library, so just keep it as one package
options = ["!lintstatic"]
