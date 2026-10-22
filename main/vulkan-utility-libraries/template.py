pkgname = "vulkan-utility-libraries"
pkgver = "1.4.365"
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
sha256 = "257a8069bac42663471af2eda04901fd195c44eb92badab55124001215151857"
# broken cmake files
tool_flags = {"CXXFLAGS": ["-I/usr/include/magic_enum"]}
# static-only library, so just keep it as one package
options = ["!lintstatic"]
