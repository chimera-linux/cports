pkgname = "libzmq"
pkgver = "4.3.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-libbsd"]
hostmakedepends = [
    "asciidoc",
    "automake",
    "libtool",
    "pkgconf",
    "xmlto",
]
makedepends = [
    "libsodium-devel",
]
pkgdesc = "ZeroMQ messaging library and tools"
license = "MPL-2.0"
url = "https://zeromq.org"
source = f"https://github.com/zeromq/libzmq/releases/download/v{pkgver}/zeromq-{pkgver}.tar.gz"
sha256 = "6653ef5910f17954861fe72332e68b03ca6e4d9c7160eb3a8de5a5a913bfab43"


@subpackage("libzmq-devel")
def _(self):
    return self.default_devel()
