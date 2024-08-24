pkgname = "hardened_malloc"
pkgver = "12"
pkgrel = 0
build_style = "makefile"
make_build_args = [
    "CONFIG_NATIVE=false",
    "CONFIG_WERROR=false",
]
make_check_target = "test"
make_use_env = True
checkdepends = ["python"]
pkgdesc = "Hardened allocator to catch allocator-related errors"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/GrapheneOS/hardened_malloc"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "0bc99987ff149455cd790b1f99566094baeb2212c5ec116ac526685999a29db5"


def do_install(self):
    self.install_license("LICENSE")
    self.install_lib("out/libhardened_malloc.so")
