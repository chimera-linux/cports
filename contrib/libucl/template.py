pkgname = "libucl"
pkgver = "0.9.2"
pkgrel = 0
build_style = "gnu_configure"
configure_env = {"NOCONFIGURE": "1"}
configure_gen = ["./autogen.sh"]
make_cmd = "gmake"
hostmakedepends = ["automake", "libtool", "gmake", "pkgconf"]
makedepends = ["openssl-devel"]
pkgdesc = "Universal configuration library parser"
maintainer = "ttyyls <contact@behri.org>"
license = "BSD-2-Clause"
url = "https://github.com/vstakhov/libucl"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f63ddee1d7f5217cac4f9cdf72b9c5e8fe43cfe5725db13f1414b0d8a369bbe0"


def post_install(self):
    self.install_license("COPYING")
    self.install_man("doc/libucl.3")


@subpackage("libucl-devel")
def _devel(self):
    return self.default_devel()
