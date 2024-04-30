pkgname = "intel-media-driver"
pkgver = "24.2.2"
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
sha256 = "7d0d43e201706ab2dc62741b7873d52dc3779a7b1187b5a321cd0a37223b2b8c"
# FIXME: cfi
hardening = ["vis"]
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("intel-media-driver-devel")
def _devel(self):
    return self.default_devel()
