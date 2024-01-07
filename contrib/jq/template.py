pkgname = "jq"
pkgver = "1.7.1"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = [
    "automake",
    "autoconf",
    "gmake",
    "libtool",
    "pkgconf",
]
makedepends = ["oniguruma-devel"]
pkgdesc = "Command-line JSON processor"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/jqlang/jq"
source = f"{url}/releases/download/jq-{pkgver}/jq-{pkgver}.tar.gz"
sha256 = "478c9ca129fd2e3443fe27314b455e211e0d8c60bc8ff7df703873deeee580c2"
# FIXME int: null meme in jqtest
hardening = ["!int", "vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("jq-devel")
def _devel(self):
    return self.default_devel()


@subpackage("jq-libs")
def _libs(self):
    return self.default_libs()
