pkgname = "vulkan-utility-libraries"
pkgver = "1.4.334"
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
license = "Apache-2.0"
url = "https://github.com/KhronosGroup/Vulkan-Utility-Libraries"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "444fa580290bc7e3bb2d098648478a79ee85b4a1ca5f852e58fd64798a36c498"
# broken cmake files
tool_flags = {"CXXFLAGS": ["-I/usr/include/magic_enum"]}
# static-only library, so just keep it as one package
options = ["!lintstatic"]
