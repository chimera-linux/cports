pkgname = "telescope"
pkgver = "0.10.1"
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
maintainer = "ttyyls <contact@behri.org>"
license = "ISC AND Unicode-3.0 AND BSD-3-Clause AND MIT"
url = "https://www.telescope-browser.org"
source = f"https://ftp.omarpolo.com/telescope-{pkgver}.tar.gz"
sha256 = "01446a1129741c6a201c4b5446390e9331487af844cef6bfd35419989168e618"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
