pkgname = "capnproto"
pkgver = "1.2.0"
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
license = "MIT"
url = "https://capnproto.org"
source = f"{url}/capnproto-c++-{pkgver}.tar.gz"
sha256 = "ed00e44ecbbda5186bc78a41ba64a8dc4a861b5f8d4e822959b0144ae6fd42ef"


if self.profile().cross:
    hostmakedepends += ["capnproto-devel"]
    configure_args += ["-DEXTERNAL_CAPNP=ON", "-DBUILD_TESTING=OFF"]

if self.profile().arch == "armv7":
    # mutex-test.c++ has timing issues
    make_check_args = ["-E", "kj-tests-run"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("capnproto-devel")
def _(self):
    return self.default_devel(extra=["usr/bin"])
