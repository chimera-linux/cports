pkgname = "tmux"
pkgver = "3.3a"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--prefix=/usr"]
hostmakedepends = ["byacc", "pkgconf"]
makedepends = ["libevent-devel", "ncurses-devel"]
pkgdesc = "Terminal multiplexer"
maintainer = "Justin Berthault <justin.berthault@zaclys.net>"
license = "ISC"
url = "https://tmux.github.io"
source = f"https://github.com/tmux/tmux/releases/download/{pkgver}/tmux-{pkgver}.tar.gz"
sha256 = "e4fd347843bd0772c4f48d6dde625b0b109b7a380ff15db21e97c11a4dcdf93f"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")


configure_gen = []
