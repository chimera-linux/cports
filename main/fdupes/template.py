pkgname = "fdupes"
pkgver = "2.4.0"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
makedepends = ["ncurses-devel", "pcre2-devel", "sqlite-devel"]
pkgdesc = "Tool for identifying and/or deleting duplicate files"
license = "MIT"
url = "https://github.com/adrianlopezroche/fdupes"
source = f"{url}/releases/download/v{pkgver}/fdupes-{pkgver}.tar.gz"
sha256 = "527b27a39d031dcbe1d29a220b3423228c28366c2412887eb72c25473d7b1736"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("README")
