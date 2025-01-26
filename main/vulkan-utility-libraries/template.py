pkgname = "vulkan-utility-libraries"
pkgver = "1.4.306"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/KhronosGroup/Vulkan-Utility-Libraries"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "8e60c2a92677d18a5f2417479b3ae0df65c66ab1d52e8918de175460a4c86a8a"
# broken cmake files
tool_flags = {"CXXFLAGS": ["-I/usr/include/magic_enum"]}
# static-only library, so just keep it as one package
options = ["!lintstatic"]
