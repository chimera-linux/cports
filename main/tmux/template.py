pkgname = "tmux"
pkgver = "3.4"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "byacc", "pkgconf"]
makedepends = ["libevent-devel", "ncurses-devel"]
pkgdesc = "Terminal multiplexer"
maintainer = "Justin Berthault <justin.berthault@zaclys.net>"
license = "ISC"
url = "https://tmux.github.io"
source = f"https://github.com/tmux/tmux/releases/download/{pkgver}/tmux-{pkgver}.tar.gz"
sha256 = "551ab8dea0bf505c0ad6b7bb35ef567cdde0ccb84357df142c254f35a23e19aa"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
