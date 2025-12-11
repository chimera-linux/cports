pkgname = "libfido2-bootstrap"
pkgver = "1.16.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBOOTSTRAP=TRUE",
    "-DBUILD_EXAMPLES=OFF",
    "-DBUILD_MANPAGES=OFF",
    "-DBUILD_TOOLS=OFF",
    "-DBUILD_STATIC_LIBS=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "libcbor-devel",
    "linux-headers",
    "openssl3-devel",
    "zlib-ng-compat-devel",
]
depends = ["!libfido2", "!libfido2-devel"]
provides = ["so:libfido2.so.1=0", "pc:libfido2=0"]
pkgdesc = "Version of libfido2 for bootstrap purposes"
license = "BSD-2-Clause"
url = "https://developers.yubico.com/libfido2"
source = f"{url}/Releases/libfido2-{pkgver}.tar.gz"
sha256 = "8c2b6fb279b5b42e9ac92ade71832e485852647b53607c43baaafbbcecea04e4"
# check is pointless here
options = ["!check", "!scanshlibs", "!scanpkgconf"]


def post_install(self):
    self.install_license("LICENSE")
