pkgname = "capnproto"
pkgver = "1.1.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "libucontext-devel",
    "linux-headers",
    "openssl3-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Cap'n Proto serialization/RPC system"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MIT"
url = "https://capnproto.org"
source = f"{url}/capnproto-c++-{pkgver}.tar.gz"
sha256 = "07167580e563f5e821e3b2af1c238c16ec7181612650c5901330fa9a0da50939"


if self.profile().cross:
    hostmakedepends += ["capnproto-devel"]
    configure_args += ["-DEXTERNAL_CAPNP=ON", "-DBUILD_TESTING=OFF"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("capnproto-devel")
def _(self):
    return self.default_devel(extra=["usr/bin"])
