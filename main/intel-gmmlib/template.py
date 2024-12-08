pkgname = "intel-gmmlib"
pkgver = "22.5.5"
pkgrel = 0
# aarch64 segfaults in tests
# only needed for intel-media-driver anyway
archs = ["x86_64"]
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "Intel Graphics Memory Management Library"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/intel/gmmlib"
source = f"{url}/archive/refs/tags/intel-gmmlib-{pkgver}.tar.gz"
sha256 = "08db696071510b7e03aa2d9fb7375c6c35f7c327ecd6747424c664c622bb4377"
# CFI: testsuite sigill
hardening = ["vis", "!cfi"]
# check cross: testsuite runs as part of install(), disabling that also doesn't build it..
options = ["!check", "!cross"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("intel-gmmlib-devel")
def _(self):
    return self.default_devel()
