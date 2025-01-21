pkgname = "libmaxminddb"
pkgver = "1.12.2"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = ["automake", "libtool", "pkgconf"]
pkgdesc = "Library for the MaxMind DB file format used for GeoIP2"
maintainer = "Renato Botelho do Couto <renato@netgate.com>"
license = "Apache-2.0"
url = "https://github.com/maxmind/libmaxminddb"
source = f"{url}/releases/download/{pkgver}/libmaxminddb-{pkgver}.tar.gz"
sha256 = "1bfbf8efba3ed6462e04e225906ad5ce5fe958aa3d626a1235b2a2253d600743"


@subpackage("libmaxminddb-devel")
def _(self):
    return self.default_devel()
