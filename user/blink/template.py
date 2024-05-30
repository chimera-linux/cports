pkgname = "blink"
pkgver = "1.1.0"
pkgrel = 0
build_style = "configure"
configure_args = ["--prefix=/usr"]
make_cmd = "gmake"
make_dir = "."
make_check_target = "test"
hostmakedepends = ["gmake", "pkgconf"]
makedepends = ["zlib-devel"]
pkgdesc = "Virtual machine for x86-64 Linux programs"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "ISC"
url = "https://github.com/jart/blink"
source = f"{url}/releases/download/{pkgver}/blink-{pkgver}.tar.gz"
sha256 = "9ac213c7d34a672d2077e79a2aaa85737eb1692d6e533ab2483c07369c60d834"


def post_install(self):
    self.install_license("LICENSE")
