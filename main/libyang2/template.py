pkgname = "libyang2"
pkgver = "2.2.8"
pkgrel = 0

build_style = "cmake"
hostmakedepends = [
    "bash",
    "cmake",
    "ninja",
]
makedepends = [
    "musl-devel",
    "pcre2-devel",
]

pkgdesc = "YANG library"
license = "BSD-3-Clause"

url = "https://github.com/CESNET/libyang"
source = f"https://github.com/CESNET/libyang/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "301e134acbaa1f3eb1e5db0a996ce4bc9ff32de61c98f5fe3192e6cc84429dd3"

def post_install(self):
    self.install_license("LICENSE")
