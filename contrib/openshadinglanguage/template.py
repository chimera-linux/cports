pkgname = "openshadinglanguage"
pkgver = "1.13.10.0"
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
    "zlib-devel",
]
pkgdesc = "Shading language library for renderers"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://github.com/AcademySoftwareFoundation/OpenShadingLanguage"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "302f573d21c700d859fb36497d377656cb51213309d95bebda941bb0993a7f42"
# set in rel
tool_flags = {"CFLAGS": ["-DNDEBUG"], "CXXFLAGS": ["-DNDEBUG"]}
# CFI: instantly crashes
# INT: guilty until proven innocent
hardening = ["vis", "!cfi", "!int"]
# checks require cpu features
options = ["linkundefver"]

if self.profile().arch not in ["ppc64le", "x86_64"]:
    options += ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("openshadinglanguage-devel")
def _devel(self):
    return self.default_devel()


@subpackage("openshadinglanguage-progs")
def _progs(self):
    return self.default_progs()
