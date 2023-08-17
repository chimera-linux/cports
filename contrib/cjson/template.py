pkgname = "cjson"
pkgver = "1.7.16"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_AND_STATIC_LIBS=ON",
    # only warnings and werror
    "-DENABLE_CUSTOM_COMPILER_FLAGS=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "Lightweight C JSON parser"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/DaveGamble/cJSON"
source = (
    f"https://github.com/DaveGamble/cJSON/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "451131a92c55efc5457276807fc0c4c2c2707c9ee96ef90c47d68852d5384c6c"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("cjson-devel")
def _devel(self):
    return self.default_devel()
