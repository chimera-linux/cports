pkgname = "metee"
pkgver = "5.0.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = [
    "cmake",
    "ninja",
]
makedepends = ["linux-headers"]
pkgdesc = "Intel CSME HECI interface access library"
license = "Apache-2.0"
url = "https://github.com/intel/metee"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "b18810875ab2e13ffe10afed54f99974ad75fbed536c680d7d1950bb90b20d68"


@subpackage("metee-devel")
def _(self):
    return self.default_devel()
