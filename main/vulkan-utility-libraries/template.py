pkgname = "vulkan-utility-libraries"
pkgver = "1.3.300"
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
sha256 = "ffc35127708e1fa94f97ed356b645c4a93e1dfbf8e9d39e48a1d27685a3899fb"
# static-only library, so just keep it as one package
options = ["!lintstatic"]
