pkgname = "vulkan-utility-libraries"
pkgver = "1.4.317"
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
sha256 = "b2ebc07892bfbde4e15288b73d5406dd0bed83a889775b4738aa06daac90d02d"
# broken cmake files
tool_flags = {"CXXFLAGS": ["-I/usr/include/magic_enum"]}
# static-only library, so just keep it as one package
options = ["!lintstatic"]
