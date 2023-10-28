pkgname = "intel-media-driver"
pkgver = "23.4.0"
pkgrel = 0
# doesn't build elsewhere
archs = ["x86_64"]
build_style = "cmake"
configure_args = [
    "-DINSTALL_DRIVER_SYSCONF=OFF",
    "-DMEDIA_BUILD_FATAL_WARNINGS=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "intel-gmmlib-devel",
    "libpciaccess-devel",
    "libva-devel",
    "libx11-devel",
    "linux-headers",
]
pkgdesc = "Intel Media Driver for VAAPI"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://github.com/intel/media-driver"
source = f"https://github.com/intel/media-driver/archive/refs/tags/intel-media-{pkgver}.tar.gz"
sha256 = "716a30d9ec652edf2b901aaa70c91c5618434b0980a7767b17a31edd49459627"
# FIXME: cfi
hardening = ["vis"]
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("intel-media-driver-devel")
def _devel(self):
    return self.default_devel()
