# update and rebuild shaderc when updating
pkgname = "spirv-tools"
pkgver = "1.4.357.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DSPIRV_WERROR=OFF",
    f"-DSPIRV-Headers_SOURCE_DIR={self.profile().sysroot / 'usr'}",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "python"]
makedepends = ["spirv-headers"]
pkgdesc = "API and commands for processing SPIR-V modules"
license = "Apache-2.0"
url = "https://github.com/KhronosGroup/SPIRV-Tools"
source = f"{url}/archive/vulkan-sdk-{pkgver}.tar.gz"
sha256 = "d31e7109b6ef3559067e53e520870eafed7c9534d00db9728814b6df03fa4a5e"
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
    self.renames = ["libspirv-tools-shared"]

    return ["usr/lib/*.so"]


@subpackage("spirv-tools-devel")
def _(self):
    self.depends += [
        self.parent,
        self.with_pkgver(f"{pkgname}-devel-static"),
        self.with_pkgver(f"{pkgname}-libs"),
    ]

    return self.default_devel()
