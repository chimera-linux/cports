pkgname = "capnproto"
pkgver = "1.0.2"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "libucontext-devel",
    "linux-headers",
    "openssl-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Cap'n Proto serialization/RPC system"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MIT"
url = "https://capnproto.org"
source = f"{url}/capnproto-c++-{pkgver}.tar.gz"
sha256 = "9057dbc0223366b74bbeca33a05de164a229b0377927f1b7ef3828cdd8cb1d7e"


if self.profile().cross:
    hostmakedepends += ["capnproto-devel"]
    configure_args += ["-DEXTERNAL_CAPNP=ON", "-DBUILD_TESTING=OFF"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("capnproto-devel")
def _(self):
    return self.default_devel(extra=["usr/bin"])
