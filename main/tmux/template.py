pkgname = "tmux"
pkgver = "3.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-sixel"]
hostmakedepends = ["automake", "byacc", "pkgconf"]
makedepends = ["libevent-devel", "ncurses-devel"]
pkgdesc = "Terminal multiplexer"
maintainer = "Justin Berthault <justin.berthault@zaclys.net>"
license = "ISC"
url = "https://tmux.github.io"
source = f"https://github.com/tmux/tmux/releases/download/{pkgver}/tmux-{pkgver}.tar.gz"
sha256 = "2fe01942e7e7d93f524a22f2c883822c06bc258a4d61dba4b407353d7081950f"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
