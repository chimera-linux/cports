pkgname = "capstone"
pkgver = "5.0.2"
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
sha256 = "9d0be727cc942075a1696f576b88918eb0daf9db7a02f563f0c4e51a439a611d"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE.TXT")


@subpackage("capstone-devel")
def _devel(self):
    return self.default_devel()


@subpackage("capstone-progs")
def _progs(self):
    return self.default_progs()
