pkgname = "protobuf-c"
pkgver = "1.5.2"
pkgrel = 3
build_style = "gnu_configure"
configure_args = [
    "--enable-protoc",
]
hostmakedepends = ["automake", "slibtool", "pkgconf", "protobuf-protoc"]
makedepends = ["boost-devel", "protobuf-devel"]
pkgdesc = "Protobuf implementation in C"
license = "BSD-2-Clause"
url = "https://github.com/protobuf-c/protobuf-c"
source = f"{url}/releases/download/v{pkgver}/protobuf-c-{pkgver}.tar.gz"
sha256 = "e2c86271873a79c92b58fef7ebf8de1aa0df4738347a8bd5d4e65a80a16d0d24"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("protobuf-c-devel")
def _(self):
    return self.default_devel(extra=["usr/bin"])
