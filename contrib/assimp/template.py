pkgname = "assimp"
pkgver = "5.4.2"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://www.assimp.org"
source = f"https://github.com/assimp/assimp/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7414861a7b038e407b510e8b8c9e58d5bf8ca76c9dfe07a01d20af388ec5086a"
hardening = ["vis", "!cfi"]


def do_check(self):
    self.do(f"{self.make_dir}/bin/unit")


def post_install(self):
    self.install_license("LICENSE")


@subpackage("assimp-devel")
def _devel(self):
    self.depends += ["minizip-devel", "zlib-ng-compat-devel"]
    return self.default_devel()


@subpackage("assimp-progs")
def _progs(self):
    return self.default_progs()
