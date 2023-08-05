pkgname = "jq"
pkgver = "1.6"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
make_dir = "."
hostmakedepends = [
    "automake",
    "autoconf",
    "gmake",
    "libtool",
]
makedepends = ["oniguruma-devel"]
pkgdesc = "Command-line JSON processor"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/jqlang/jq"
source = f"{url}/releases/download/jq-{pkgver}/jq-{pkgver}.tar.gz"
sha256 = "5de8c8e29aaa3fb9cc6b47bb27299f271354ebb72514e3accadc7d38b5bbaa72"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("jq-devel")
def _devel(self):
    return self.default_devel()


@subpackage("jq-libs")
def _libs(self):
    return self.default_libs()
