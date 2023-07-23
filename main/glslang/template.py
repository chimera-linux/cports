# note: some libs are unversioned (rebuild shaderc on updates)
pkgname = "glslang"
pkgver = "12.3.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = ["cmake", "ninja", "python", "bison"]
checkdepends = ["bash"]
pkgdesc = "Khronos reference front-end for GLSL/ESSL + sample SPIR-V generator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/KhronosGroup/glslang"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "a57836a583b3044087ac51bb0d5d2d803ff84591d55f89087fc29ace42a8b9a8"
# missing checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
    # for whatever reason this does not get installed?
    self.install_link("glslang", "usr/bin/glslangValidator")


@subpackage("glslang-progs")
def _progs(self):
    return self.default_progs()


@subpackage("glslang-devel-static")
def _devstatic(self):
    self.pkgdesc = f"{pkgdesc} (static development libraries)"
    self.depends = []
    self.install_if = []

    return ["usr/lib/*.a"]


@subpackage("glslang-devel")
def _devel(self):
    self.options = ["!splitstatic"]
    self.depends += [f"glslang-devel-static={pkgver}-r{pkgrel}"]

    return [
        "usr/include",
        "usr/lib/libglslang.so",
        "usr/lib/cmake",
    ]
