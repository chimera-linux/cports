pkgname = "capstone"
pkgver = "5.0.5"
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
sha256 = "3bfd3e7085fbf0fab75fb1454067bf734bb0bebe9b670af7ce775192209348e9"
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE.TXT")


@subpackage("capstone-devel")
def _(self):
    return self.default_devel()


@subpackage("capstone-progs")
def _(self):
    return self.default_progs()
