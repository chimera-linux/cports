pkgname = "intel-gmmlib"
pkgver = "22.8.2"
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
license = "MIT"
url = "https://github.com/intel/gmmlib"
source = f"{url}/archive/refs/tags/intel-gmmlib-{pkgver}.tar.gz"
sha256 = "2e43e538a002574f45d480a24e02297c960963dc7914b7328791d9836832ff43"
# CFI: testsuite sigill
hardening = ["vis", "!cfi"]
# check cross: testsuite runs as part of install(), disabling that also doesn't build it..
options = ["!check", "!cross"]


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("intel-gmmlib-devel")
def _(self):
    return self.default_devel()
