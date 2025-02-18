pkgname = "libmodule"
pkgver = "5.0.2"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_TESTS=ON"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
checkdepends = ["cmocka-devel"]
pkgdesc = "Actor library for C"
license = "MIT"
url = "https://github.com/FedeDP/libmodule"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "72101e69aabe16937576fa30a61830309b28ce96aa3bb7de5958134fa521f7fe"


@subpackage("libmodule-devel")
def _(self):
    return self.default_devel()
