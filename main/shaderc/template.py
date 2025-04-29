pkgname = "shaderc"
pkgver = "2025.2"
pkgrel = 1
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
sha256 = "3fddc13bbb87411c6f7b8f447e87c1637933450087e70fc21da650041f4e0132"
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
