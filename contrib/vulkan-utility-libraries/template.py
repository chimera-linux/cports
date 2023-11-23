pkgname = "vulkan-utility-libraries"
pkgver = "1.3.270"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
makedepends = ["vulkan-headers"]
pkgdesc = "Vulkan Utility Libraries"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "Apache-2.0"
url = "https://www.khronos.org/vulkan"
source = f"https://github.com/KhronosGroup/Vulkan-Utility-Libraries/archive/v{pkgver}.tar.gz"
sha256 = "c402174add9146e3238104dbf18e50385129ff2ef252ebae49b3c5f61ccc0286"


@subpackage(f"{pkgname}-devel-static")
def _devel_static(self):
    self.pkgdesc = f"{pkgdesc} (static libraries)"
    self.depends = []
    self.install_if = []

    return ["usr/lib/*.a"]
