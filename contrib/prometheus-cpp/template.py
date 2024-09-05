pkgname = "prometheus-cpp"
pkgver = "1.2.4"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["libcurl-devel", "zlib-ng-compat-devel"]
pkgdesc = "Prometheus Client Library for Modern C++"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/jupp0r/prometheus-cpp"
source = f"https://github.com/jupp0r/prometheus-cpp/releases/download/v{pkgver}/prometheus-cpp-with-submodules.tar.gz>prometheus-cpp-{pkgver}.tar.gz"
sha256 = "0d6852291063c35853e88805c73b52f73c0c08b78c1e7bc4d588fcf72a7172eb"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("prometheus-cpp-devel")
def _(self):
    return self.default_devel()
