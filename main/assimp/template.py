pkgname = "assimp"
pkgver = "6.0.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DASSIMP_BUILD_ASSIMP_TOOLS=ON",
    "-DASSIMP_BUILD_TESTS=ON",
    "-DASSIMP_IGNORE_GIT_HASH=ON",
    "-DASSIMP_WARNINGS_AS_ERRORS=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "minizip-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Open asset importing library"
license = "BSD-3-Clause"
url = "https://www.assimp.org"
source = f"https://github.com/assimp/assimp/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d1822d9a19c9205d6e8bc533bf897174ddb360ce504680f294170cc1d6319751"
hardening = ["vis", "!cfi"]


def check(self):
    self.do(f"{self.make_dir}/bin/unit")


def post_install(self):
    self.install_license("LICENSE")


@subpackage("assimp-devel")
def _(self):
    self.depends += ["minizip-devel", "zlib-ng-compat-devel"]
    return self.default_devel()


@subpackage("assimp-progs")
def _(self):
    return self.default_progs()
