pkgname = "mtxclient"
pkgver = "0.10.1"
pkgrel = 1
build_style = "cmake"
configure_args = ["-DBUILD_LIB_EXAMPLES=OFF"]
make_check_args = [
    "-E",
    # need net
    "(BasicConnectivity|ClientAPI|MediaAPI|Encryption|Devices|Pushrules)",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "coeurl-devel",
    "curl-devel",
    "gtest-devel",
    "libevent-devel",
    "nlohmann-json",
    "olm-devel",
    "openssl3-devel",
    "re2-devel",
]
pkgdesc = "Client API library for the Matrix protocol"
license = "MIT"
url = "https://github.com/nheko-reborn/mtxclient"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "203be46a08e1dc6cfc068d0911f3b09976f48e4cc4302c3517b9c0f4e53631e3"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("mtxclient-devel")
def _(self):
    return self.default_devel()
