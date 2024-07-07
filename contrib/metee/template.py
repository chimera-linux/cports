pkgname = "metee"
pkgver = "4.1.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = ["linux-headers"]
pkgdesc = "Intel CSME HECI interface access library"
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0"
url = "https://github.com/intel/metee"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f50ff7e42e9a0c6a133f706f009fc3e6c3704b1291ccb499ca136825e3b3aa98"


@subpackage("metee-devel")
def _devel(self):
    return self.default_devel()
