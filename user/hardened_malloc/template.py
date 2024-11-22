pkgname = "hardened_malloc"
pkgver = "13"
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
sha256 = "1c485dbfd397db68081f95182cde18e1fa54a091dca7e67ee8c9356c6c5db798"


def install(self):
    self.install_license("LICENSE")
    self.install_lib("out/libhardened_malloc.so")
