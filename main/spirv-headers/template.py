pkgname = "spirv-headers"
# a recent snapshot is needed, latest tagged release is not good enough
# for spirv-llvm-translator and without it we cannot build libclc
_commit = "eddd4dfc930f1374a70797460240a501c7d333f7"
# actually not the real version
pkgver = "1.5.4"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Machine-readable files for the SPIR-V Registry"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:spirv-headers"
url = "https://github.com/KhronosGroup/SPIRV-Headers"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "845c29d7f44bd6c5bb7ddefba93deec888ce03439d3b8a1c1388e34fd7c13944"
# no test suite
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
