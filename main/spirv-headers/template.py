pkgname = "spirv-headers"
# a recent snapshot is needed, latest tagged release is not good enough
# for spirv-llvm-translator and without it we cannot build libclc
_commit = "29817199b7069bac971e5365d180295d4b077ebe"
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
sha256 = "b96e9a0bb6468f80c50f05a34c4eb690f5951d8d73ee1615ce0df417d755bfb9"
# no test suite
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE")
