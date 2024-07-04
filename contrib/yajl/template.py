pkgname = "yajl"
pkgver = "2.1.0"
pkgrel = 0
build_style = "cmake"
make_check_target = "test test-api"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "Yet Another JSON Library"
maintainer = "psykose <alice@ayaya.dev>"
license = "ISC"
url = "https://github.com/lloyd/yajl"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "3fb73364a5a30efe615046d07e6db9d09fd2b41c763c5f7d3bfb121cd5c5ac5a"
# FIXME: cfi crashes in test-api
hardening = ["vis"]


def post_install(self):
    self.install_license("COPYING")
    self.rename("usr/lib/libyajl_s.a", "libyajl.a")


@subpackage("yajl-devel")
def _devel(self):
    return self.default_devel()


@subpackage("yajl-libs")
def _libs(self):
    return self.default_libs()
