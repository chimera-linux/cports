pkgname = "shaderc"
pkgver = "2025.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DSHADERC_SKIP_TESTS=ON",
    "-DSHADERC_SKIP_EXAMPLES=ON",
]
hostmakedepends = ["cmake", "ninja", "python", "pkgconf"]
makedepends = ["spirv-tools-devel", "spirv-headers", "glslang-devel"]
pkgdesc = "Collection of tools and libraries for shader compilation"
license = "Apache-2.0"
url = "https://github.com/google/shaderc"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "8a89fb6612ace8954470aae004623374a8fc8b7a34a4277bee5527173b064faf"
tool_flags = {
    "CXXFLAGS": [f"-I{self.profile().sysroot / 'usr/include/glslang'}"]
}
hardening = ["!vis", "!cfi"]


@subpackage("shaderc-progs")
def _(self):
    return self.default_progs()


@subpackage("shaderc-devel")
def _(self):
    return self.default_devel()
