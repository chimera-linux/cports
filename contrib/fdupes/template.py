pkgname = "fdupes"
pkgver = "2.3.1"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
makedepends = ["ncurses-devel", "pcre2-devel", "sqlite-devel"]
pkgdesc = "Tool for identifying and/or deleting duplicate files"
maintainer = "autumnontape <autumn@cyfox.net>"
license = "MIT"
url = "https://github.com/adrianlopezroche/fdupes"
source = f"{url}/releases/download/v{pkgver}/fdupes-{pkgver}.tar.gz"
sha256 = "2482b4b8c931bd17cea21f4c27fa4747b877523029d57f794a2b48e6c378db17"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("README")
