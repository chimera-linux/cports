pkgname = "telescope"
pkgver = "0.11"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-default-editor=vi"]
make_dir = "."
hostmakedepends = ["automake", "bison", "pkgconf"]
makedepends = [
    "libgrapheme-devel",
    "libretls-devel",
    "ncurses-devel",
    "openssl3-devel",
]
pkgdesc = "Terminal browser for gemini/gopher/finger"
license = "ISC AND Unicode-3.0 AND BSD-3-Clause AND MIT"
url = "https://www.telescope-browser.org"
source = f"https://ftp.telescope-browser.org/telescope-{pkgver}.tar.gz"
sha256 = "0b56fc56958d4b4c2ecc7dc971d4f7c156ca827d5bd97b70dcb541cf9e423927"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
