pkgname = "libkcapi"
pkgver = "1.5.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-werror",
    "--enable-lib-asym",
    "--enable-lib-kpp",
]
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = ["linux-headers"]
checkdepends = ["bash", "openssl"]
pkgdesc = "Linux Kernel Crypto API User Space Interface Library"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause OR GPL-2.0-only"
url = "https://www.chronox.de/libkcapi/index.html"
source = (
    f"https://github.com/smuellerDD/libkcapi/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "f1d827738bda03065afd03315479b058f43493ab6e896821b947f391aa566ba0"
# bunch of unportable shellscript nonsense
options = ["linkundefver", "!check"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libkcapi-devel")
def _devel(self):
    return self.default_devel()
