# update and rebuild shaderc when updating
pkgname = "spirv-tools"
pkgver = "1.3.296.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DSPIRV_WERROR=OFF",
    f"-DSPIRV-Headers_SOURCE_DIR={self.profile().sysroot / 'usr'}",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "python"]
makedepends = ["spirv-headers"]
pkgdesc = "API and commands for processing SPIR-V modules"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/KhronosGroup/SPIRV-Tools"
source = f"{url}/archive/vulkan-sdk-{pkgver}.tar.gz"
sha256 = "75aafdf7e731b4b6bfb36a590ddfbb38ebc605d80487f38254da24fe0cb95837"
hardening = ["!vis", "!cfi"]

# Note: only some tests are run, the others need subfolders of gtest and effcee
# and some other stuff


@subpackage("spirv-tools-devel-static")
def _(self):
    self.depends = []
    self.install_if = []

    return ["usr/lib/*.a"]


@subpackage("libspirv-tools-shared")
def _(self):
    self.subdesc = "shared library"

    return ["usr/lib/*.so"]


@subpackage("spirv-tools-devel")
def _(self):
    self.depends += [
        self.parent,
        self.with_pkgver(f"{pkgname}-devel-static"),
        self.with_pkgver(f"lib{pkgname}-shared"),
    ]

    return self.default_devel()
