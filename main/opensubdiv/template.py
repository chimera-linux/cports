pkgname = "opensubdiv"
pkgver = "3.6.0"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "Apache-2.0"
url = "https://graphics.pixar.com/opensubdiv/docs/intro.html"
source = f"https://github.com/PixarAnimationStudios/OpenSubdiv/archive/refs/tags/v{pkgver.replace('.', '_')}.tar.gz"
sha256 = "bebfd61ab6657a4f4ff27845fb66a167d00395783bfbd253254d87447ed1d879"


@subpackage("opensubdiv-devel")
def _(self):
    return self.default_devel()


@subpackage("opensubdiv-progs")
def _(self):
    return self.default_progs()
