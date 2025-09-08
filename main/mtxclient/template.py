pkgname = "mtxclient"
pkgver = "0.10.0"
pkgrel = 7
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
sha256 = "9502e0a999d2873172d50bb80371c061266126c7d4db8e44447eb70c977b0230"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("mtxclient-devel")
def _(self):
    return self.default_devel()
