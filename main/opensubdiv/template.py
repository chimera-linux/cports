pkgname = "opensubdiv"
pkgver = "3.7.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DNO_CLEW=ON",
    "-DNO_CUDA=ON",
    "-DNO_DOC=ON",
    "-DNO_EXAMPLES=ON",
    "-DNO_GLTESTS=ON",
    "-DNO_PTEX=ON",
    "-DNO_TUTORIALS=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = [
    "glfw-devel",
    "libomp-devel",
    "libxcursor-devel",
    "libxi-devel",
    "libxinerama-devel",
    "libxrandr-devel",
    "libxxf86vm-devel",
    "mesa-devel",
    "ocl-icd-devel",
    "onetbb-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Surface subdivision library"
license = "Apache-2.0"
url = "https://graphics.pixar.com/opensubdiv/docs/intro.html"
source = f"https://github.com/PixarAnimationStudios/OpenSubdiv/archive/refs/tags/v{pkgver.replace('.', '_')}.tar.gz"
sha256 = "f843eb49daf20264007d807cbc64516a1fed9cdb1149aaf84ff47691d97491f9"
# for some reason libomp does not make it in?
tool_flags = {"LDFLAGS": ["-lomp"]}


@subpackage("opensubdiv-devel")
def _(self):
    return self.default_devel()


@subpackage("opensubdiv-progs")
def _(self):
    return self.default_progs()
