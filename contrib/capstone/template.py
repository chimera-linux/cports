pkgname = "capstone"
pkgver = "5.0.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = [
    "bash",
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "Ultimate Disassembler"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause-Clear"
url = "https://www.capstone-engine.org"
source = f"https://github.com/capstone-engine/capstone/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "2b9c66915923fdc42e0e32e2a9d7d83d3534a45bb235e163a70047951890c01a"
# FIXME: cfi
hardening = ["vis"]


def post_install(self):
    self.install_license("LICENSE.TXT")


@subpackage("capstone-devel")
def _devel(self):
    return self.default_devel()


@subpackage("capstone-progs")
def _progs(self):
    return self.default_progs()
