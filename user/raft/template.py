pkgname = "raft"
pkgver = "0.22.1"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
]
makedepends = ["linux-headers", "libuv-devel", "lz4-devel"]
pkgdesc = "C implementation of the Raft consensus protocol"
license = "LGPL-3.0-only"
url = "https://github.com/cowsql/raft"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "385f91a0b542ebe8b81c8f8500310dcd575fd028ea0cd2ede8807fa920dcf604"


@subpackage("raft-devel")
def _(self):
    return self.default_devel()
