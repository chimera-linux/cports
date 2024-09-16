pkgname = "fnc"
pkgver = "0.18"
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
sha256 = "49f94c67e00213440d84f3b09bcf75850f9b6e8d8721856d68f4596c49cec780"
# no tests
options = ["!check"]


def install(self):
    self.install_bin("src/fnc")
    self.install_man("src/fnc.1")
    self.install_license("LICENSE")
