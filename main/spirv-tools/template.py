# update and rebuild shaderc when updating
pkgname = "spirv-tools"
pkgver = "1.4.328.1"
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
sha256 = "d00dc47df7163c2bacd70f090441e8fad96234f0e3b96c54ee9091a49e627adb"
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
