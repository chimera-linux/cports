pkgname = "libipt"
pkgver = "2.2"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DPTUNIT=ON"]
hostmakedepends = ["cmake", "meson"]
pkgdesc = "Intel Processor Trace decoder library"
license = "BSD-3-Clause"
url = "https://github.com/intel/libipt"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f09a18fefba81d4fc2530d90858789e0c596f1b634e5777e6ccaf492966e9845"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libipt-devel")
def _(self):
    return self.default_devel()
