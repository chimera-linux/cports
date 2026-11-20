pkgname = "opentmux"
pkgver = "0.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-sixel", "--enable-kitty"]
hostmakedepends = ["automake", "byacc", "pkgconf"]
makedepends = ["libevent-devel", "ncurses-devel"]
provides = ["tmux=3.6a"]
pkgdesc = "Terminal multiplexer, fork of tmux without LLM-code"
license = "ISC"
url = "https://codeberg.org/opentmux/opentmux"
source = f"{url}/releases/download/v{pkgver}/opentmux-{pkgver}.tar.gz"
sha256 = "771f729b1c43722007d0f481208acf0f9a0168c904168cf682d718355ce60689"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("COPYING")
