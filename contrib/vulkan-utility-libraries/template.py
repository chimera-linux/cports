pkgname = "vulkan-utility-libraries"
pkgver = "1.3.291"
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
sha256 = "6678ccafae4868947ad155058dd5524e4ee3c1ccc04f8f42241cd05ec41a2526"
# static-only library, so just keep it as one package
options = ["!lintstatic"]
