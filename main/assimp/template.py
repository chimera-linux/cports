pkgname = "assimp"
pkgver = "5.4.3"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://www.assimp.org"
source = f"https://github.com/assimp/assimp/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "66dfbaee288f2bc43172440a55d0235dfc7bf885dda6435c038e8000e79582cb"
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
