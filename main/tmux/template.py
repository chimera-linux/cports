pkgname = "tmux"
pkgver = "3.6a"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-sixel"]
hostmakedepends = ["automake", "byacc", "pkgconf"]
makedepends = ["libevent-devel", "ncurses-devel"]
pkgdesc = "Terminal multiplexer"
license = "ISC"
url = "https://tmux.github.io"
source = f"https://github.com/tmux/tmux/releases/download/{pkgver}/tmux-{pkgver}.tar.gz"
sha256 = "b6d8d9c76585db8ef5fa00d4931902fa4b8cbe8166f528f44fc403961a3f3759"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
