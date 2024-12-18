pkgname = "shaderc"
pkgver = "2024.4"
pkgrel = 0
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
sha256 = "989a46c0bc0e58ab8ac9ef9c1fb8000e0209d482b242a514b385d8f8c4cbfa06"
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
