pkgname = "fdupes"
pkgver = "2.3.0"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
makedepends = ["ncurses-devel", "pcre2-devel", "sqlite-devel"]
pkgdesc = "Tool for identifying and/or deleting duplicate files"
maintainer = "autumnontape <autumn@cyfox.net>"
license = "MIT"
url = "https://github.com/adrianlopezroche/fdupes"
source = f"{url}/releases/download/v{pkgver}/fdupes-{pkgver}.tar.gz"
sha256 = "6170d64a7e565ee314cca4dd25a123e60aa1e3febb11e57078bebb9c1da7e019"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("README")
