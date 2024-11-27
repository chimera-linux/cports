pkgname = "cjson"
pkgver = "1.7.18"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/DaveGamble/cJSON"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3aa806844a03442c00769b83e99970be70fbef03735ff898f4811dd03b9f5ee5"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("cjson-devel")
def _(self):
    return self.default_devel()
