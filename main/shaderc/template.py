pkgname = "shaderc"
pkgver = "2023.8"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DSHADERC_SKIP_TESTS=ON",
    "-DSHADERC_SKIP_EXAMPLES=ON",
    "-DPYTHON_EXECUTABLE=python",
]
hostmakedepends = ["cmake", "ninja", "python", "pkgconf"]
makedepends = ["spirv-tools-devel", "spirv-headers", "glslang-devel"]
pkgdesc = "Collection of tools and libraries for shader compilation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/google/shaderc"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "dfec5045f30d8f6d3d3914ab5b3cc2695947f266d41261b1459177cd789308d1"
tool_flags = {
    "CXXFLAGS": [f"-I{self.profile().sysroot / 'usr/include/glslang'}"]
}
hardening = ["!cfi"]  # TODO


@subpackage("shaderc-progs")
def _progs(self):
    return self.default_progs()


@subpackage("shaderc-devel")
def _devel(self):
    return self.default_devel()
