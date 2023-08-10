pkgname = "shaderc"
pkgver = "2023.6"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DSHADERC_SKIP_TESTS=ON", "-DSHADERC_SKIP_EXAMPLES=ON"]
hostmakedepends = ["cmake", "ninja", "python", "pkgconf"]
makedepends = ["spirv-tools-devel", "spirv-headers", "glslang-devel"]
pkgdesc = "Collection of tools and libraries for shader compilation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/google/shaderc"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "e40fd4a87a56f6610e223122179f086d5c4f11a7e0e2aa461f0325c3a0acc6ae"
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
