pkgname = "cjson"
pkgver = "1.7.19"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
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
license = "MIT"
url = "https://github.com/DaveGamble/cJSON"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7fa616e3046edfa7a28a32d5f9eacfd23f92900fe1f8ccd988c1662f30454562"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("cjson-devel")
def _(self):
    return self.default_devel()
