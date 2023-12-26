pkgname = "cjson"
pkgver = "1.7.17"
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
sha256 = "c91d1eeb7175c50d49f6ba2a25e69b46bd05cffb798382c19bfb202e467ec51c"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("cjson-devel")
def _devel(self):
    return self.default_devel()
