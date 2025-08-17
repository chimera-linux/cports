pkgname = "openshadinglanguage"
pkgver = "1.14.7.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_CXX_STANDARD=17",
]
make_check_args = [
    "-E",
    # fail to find test data / float diff
    "(array-range.opt"
    + "|blackbody"
    + "|example-deformer"
    + "|getattribute-shader.opt"
    + "|gettextureinfo.opt"
    + "|gettextureinfo-udim.opt"
    + "|render-displacement.opt"
    + "|render-microfacet.opt"
    + "|matrix-reg.regress.rsbitcode"
    + "|oslc-err-intoverflow"
    + "|osl-imageio"
    + "|string.opt"
    + "|texture-udim"
    + "|trig.opt"
    + "|vector.opt"
    + "|python-oslquery)",
]
hostmakedepends = [
    "bison",
    "cmake",
    "flex",
    "ninja",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "clang-devel",
    "fmt-devel",
    "llvm-devel",
    "openexr-devel",
    "openimageio-devel",
    "openimageio-progs",
    "pugixml-devel",
    "python-pybind11-devel",
    "qt6-qtbase-devel",
    "robin-map",
    "zlib-ng-compat-devel",
]
pkgdesc = "Shading language library for renderers"
license = "BSD-3-Clause"
url = "https://github.com/AcademySoftwareFoundation/OpenShadingLanguage"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c4c2ddd3b537cd3a90d50fdd0753614fa24100698d5632b9f1108bd8b505e56c"
# set in rel
tool_flags = {
    "CFLAGS": ["-DNDEBUG", "-D_LARGEFILE64_SOURCE"],
    "CXXFLAGS": ["-DNDEBUG", "-D_LARGEFILE64_SOURCE"],
}
# CFI: instantly crashes
# INT: guilty until proven innocent
hardening = ["vis", "!cfi", "!int"]
# checks require cpu features
options = ["linkundefver"]

if self.profile().arch not in ["ppc64le", "x86_64"]:
    options += ["!check"]

if self.profile().wordsize == 32:
    broken = "fails static assertions"


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("openshadinglanguage-devel")
def _(self):
    return self.default_devel()


@subpackage("openshadinglanguage-progs")
def _(self):
    return self.default_progs()


@subpackage("openshadinglanguage-python")
def _(self):
    self.subdesc = "Python modules"
    self.depends = ["openimageio-python"]
    self.renames = ["python-openshadinglanguage"]

    return ["usr/lib/python*"]
