pkgname = "kyotocabinet"
pkgver = "1.2.80"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    # march=native
    "--disable-opt",
    "--enable-lzma",
    "--enable-zlib",
]
make_dir = "."
hostmakedepends = ["automake", "pkgconf"]
makedepends = ["xz-devel", "zlib-ng-compat-devel"]
pkgdesc = "Library of database management routines"
maintainer = "metalparade <comer@live.cn>"
license = "GPL-3.0-or-later"
url = "https://dbmx.net/kyotocabinet"
source = f"{url}/pkg/kyotocabinet-{pkgver}.tar.gz"
sha256 = "4c85d736668d82920bfdbdb92ac3d66b7db1108f09581a769dd9160a02def349"


@subpackage("kyotocabinet-devel")
def _(self):
    return self.default_devel()
