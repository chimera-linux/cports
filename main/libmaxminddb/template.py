pkgname = "libmaxminddb"
pkgver = "1.11.0"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = ["automake", "libtool", "pkgconf"]
pkgdesc = "Library for the MaxMind DB file format used for GeoIP2"
maintainer = "Renato Botelho do Couto <renato@netgate.com>"
license = "Apache-2.0"
url = "https://github.com/maxmind/libmaxminddb"
source = f"{url}/releases/download/{pkgver}/libmaxminddb-{pkgver}.tar.gz"
sha256 = "b2eea79a96fed77ad4d6c39ec34fed83d45fcb75a31c58956813d58dcf30b19f"


@subpackage("libmaxminddb-devel")
def _(self):
    return self.default_devel()
