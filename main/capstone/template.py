pkgname = "capstone"
pkgver = "5.0.3"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "BSD-3-Clause-Clear"
url = "https://www.capstone-engine.org"
source = f"https://github.com/capstone-engine/capstone/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "3970c63ca1f8755f2c8e69b41432b710ff634f1b45ee4e5351defec4ec8e1753"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE.TXT")


@subpackage("capstone-devel")
def _(self):
    return self.default_devel()


@subpackage("capstone-progs")
def _(self):
    return self.default_progs()
