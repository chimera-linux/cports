pkgname = "protobuf-c"
pkgver = "1.5.1"
pkgrel = 0
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
sha256 = "20d1dc257da96f8ddff8be4dd9779215bbd0a6069ed53bbe9de38fa7629be06b"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("protobuf-c-devel")
def _(self):
    return self.default_devel(extra=["usr/bin"])
