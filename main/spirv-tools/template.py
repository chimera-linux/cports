# update and rebuild shaderc when updating
pkgname = "spirv-tools"
pkgver = "1.4.304.0"
pkgrel = 1
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
sha256 = "ad6e8922538c498e7131bcd82a8d6d9f9863b8d7431c5bfa27dd98e26435be07"
hardening = ["!vis", "!cfi"]

# Note: only some tests are run, the others need subfolders of gtest and effcee
# and some other stuff


@subpackage("spirv-tools-devel-static")
def _(self):
    self.depends = []
    self.install_if = []

    return ["usr/lib/*.a"]


@subpackage("spirv-tools-libs")
def _(self):
    self.subdesc = "shared library"
    # transitional
    self.provides = [self.with_pkgver("libspirv-tools-shared")]

    return ["usr/lib/*.so"]


@subpackage("spirv-tools-devel")
def _(self):
    self.depends += [
        self.parent,
        self.with_pkgver(f"{pkgname}-devel-static"),
        self.with_pkgver(f"{pkgname}-libs"),
    ]

    return self.default_devel()
