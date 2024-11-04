pkgname = "prometheus-cpp"
pkgver = "1.3.0"
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
sha256 = "62bc2cc9772db2314dbaae506ae2a75c8ee897dab053d8729e86a637b018fdb6"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("prometheus-cpp-devel")
def _(self):
    return self.default_devel()
