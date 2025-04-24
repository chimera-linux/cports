pkgname = "shaderc"
pkgver = "2025.1"
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
sha256 = "358f9fa87b503bc7a3efe1575fbf581fca7f16dbc6d502ea2b02628d2d0d4014"
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
