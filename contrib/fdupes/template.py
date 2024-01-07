pkgname = "fdupes"
pkgver = "2.2.1"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
makedepends = ["ncurses-devel", "pcre2-devel"]
pkgdesc = "Tool for identifying and/or deleting duplicate files"
maintainer = "autumnontape <autumn@cyfox.net>"
license = "MIT"
url = "https://github.com/adrianlopezroche/fdupes"
source = f"{url}/releases/download/v{pkgver}/fdupes-{pkgver}.tar.gz"
sha256 = "846bb79ca3f0157856aa93ed50b49217feb68e1b35226193b6bc578be0c5698d"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("README")
