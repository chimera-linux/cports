pkgname = "opentmux"
pkgver = "0.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-sixel"]
hostmakedepends = ["automake", "byacc", "pkgconf"]
makedepends = ["libevent-devel", "ncurses-devel"]
provides = ["tmux=3.6a"]
pkgdesc = "Terminal multiplexer, fork of tmux without LLM-code"
license = "ISC"
url = "https://codeberg.org/opentmux/opentmux"
source = f"{url}/releases/download/v{pkgver}/opentmux-{pkgver}.tar.gz"
sha256 = "76714adf1e3b7e592afca5852473bb3578b66165e7c03d719ec12c90bc98e62e"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
