pkgname = "tmux"
pkgver = "3.7b"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-sixel"]
hostmakedepends = ["automake", "byacc", "pkgconf"]
makedepends = ["libevent-devel", "ncurses-devel"]
pkgdesc = "Terminal multiplexer"
license = "ISC"
url = "https://tmux.github.io"
source = f"https://github.com/tmux/tmux/releases/download/{pkgver}/tmux-{pkgver}.tar.gz"
sha256 = "87f2e99e3b685973f2ca002ffd6ed7e51a5744f7009daae5a15670b6d532db96"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
