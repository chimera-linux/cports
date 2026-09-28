pkgname = "blink"
pkgver = "1.1.0"
pkgrel = 0
build_style = "configure"
configure_args = ["--prefix=/usr"]
make_dir = "."
make_check_target = "test"
hostmakedepends = ["pkgconf"]
makedepends = ["zlib-ng-compat-devel"]
pkgdesc = "Virtual machine for x86-64 Linux programs"
license = "ISC"
url = "https://github.com/jart/blink"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "2649793e1ebf12027f5e240a773f452434cefd9494744a858cd8bff8792dba68"


def post_install(self):
    self.install_license("LICENSE")
