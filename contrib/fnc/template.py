pkgname = "fnc"
pkgver = "0.16"
pkgrel = 0
build_style = "makefile"
makedepends = [
    "musl-bsd-headers",
    "ncurses-devel",
    "sqlite-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Text-based user interface for Fossil"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "ISC"
url = "https://fnc.bsdbox.org"
source = f"{url}/uv/dl/fnc-{pkgver}.tar.gz"
sha256 = "9ebfe3e9ecaa764ebc1ed488857c0a18b0f51e57a66f73620ee692587e5bf6da"
# no tests
options = ["!check"]


def install(self):
    self.install_bin("src/fnc")
    self.install_man("src/fnc.1")
    self.install_license("LICENSE")
