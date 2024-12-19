pkgname = "fdupes"
pkgver = "2.3.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf"]
makedepends = ["ncurses-devel", "pcre2-devel", "sqlite-devel"]
pkgdesc = "Tool for identifying and/or deleting duplicate files"
maintainer = "autumnontape <autumn@cyfox.net>"
license = "MIT"
url = "https://github.com/adrianlopezroche/fdupes"
source = f"{url}/releases/download/v{pkgver}/fdupes-{pkgver}.tar.gz"
sha256 = "808d8decbe7fa41cab407ae4b7c14bfc27b8cb62227540c3dcb6caf980592ac7"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("README")
