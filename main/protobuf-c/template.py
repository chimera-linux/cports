pkgname = "protobuf-c"
pkgver = "1.5.0"
pkgrel = 23
build_style = "gnu_configure"
configure_args = [
    "--enable-protoc",
]
hostmakedepends = ["automake", "slibtool", "pkgconf", "protobuf-protoc"]
makedepends = ["boost-devel", "protobuf-devel"]
pkgdesc = "Protobuf implementation in C"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/protobuf-c/protobuf-c"
source = f"{url}/releases/download/v{pkgver}/protobuf-c-{pkgver}.tar.gz"
sha256 = "7b404c63361ed35b3667aec75cc37b54298d56dd2bcf369de3373212cc06fd98"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("protobuf-c-devel")
def _(self):
    return self.default_devel(extra=["usr/bin"])
