# update and rebuild shaderc when updating
pkgname = "spirv-tools"
pkgver = "1.3.290.0"
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
sha256 = "8f8b487e20e062c3abfbc86c4541faf767588d167b395ec94f2a7f996ef40efe"
hardening = ["!vis", "!cfi"]

# Note: only some tests are run, the others need subfolders of gtest and effcee
# and some other stuff


@subpackage("spirv-tools-devel-static")
def _static(self):
    self.depends = []
    self.install_if = []

    return ["usr/lib/*.a"]


@subpackage("libspirv-tools-shared")
def _shared(self):
    self.subdesc = "shared library"

    return ["usr/lib/*.so"]


@subpackage("spirv-tools-devel")
def _devel(self):
    self.depends += [
        self.parent,
        self.with_pkgver(f"{pkgname}-devel-static"),
        self.with_pkgver(f"lib{pkgname}-shared"),
    ]

    return self.default_devel()
