pkgname = "shaderc"
pkgver = "2024.3"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DSHADERC_SKIP_TESTS=ON",
    "-DSHADERC_SKIP_EXAMPLES=ON",
]
hostmakedepends = ["cmake", "ninja", "python", "pkgconf"]
makedepends = ["spirv-tools-devel", "spirv-headers", "glslang-devel"]
pkgdesc = "Collection of tools and libraries for shader compilation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/google/shaderc"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "d5c68b5de5d4c7859d9699054493e0a42a2a5eb21b425d63f7b7dd543db0d708"
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
