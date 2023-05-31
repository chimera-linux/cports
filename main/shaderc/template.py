pkgname = "shaderc"
pkgver = "2023.4"
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
sha256 = "671c5750638ff5e42e0e0e5325b758a1ab85e6fd0fe934d369a8631c4292f12f"
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
