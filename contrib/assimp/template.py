pkgname = "assimp"
pkgver = "5.4.1"
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
    "zlib-devel",
]
pkgdesc = "Open asset importing library"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://www.assimp.org"
source = f"https://github.com/assimp/assimp/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a1bf71c4eb851ca336bba301730cd072b366403e98e3739d6a024f6313b8f954"
hardening = ["vis", "!cfi"]


def do_check(self):
    self.do(f"{self.make_dir}/bin/unit")


def post_install(self):
    self.install_license("LICENSE")


@subpackage("assimp-devel")
def _devel(self):
    self.depends += ["minizip-devel", "zlib-devel"]
    return self.default_devel()


@subpackage("assimp-progs")
def _progs(self):
    return self.default_progs()
