pkgname = "vulkan-utility-libraries"
pkgver = "1.3.296"
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
sha256 = "bea13c5f25756a9b20bc53cfbfb1a87b4a8e07ddfb7ebcdf9e173c4461d55685"
# static-only library, so just keep it as one package
options = ["!lintstatic"]
