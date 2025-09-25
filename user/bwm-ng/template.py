pkgname = "bwm-ng"
pkgver = "0.6.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-libstatgrab",
    "--with-ncurses",
    "--with-procnetdev",
]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "pkgconf",
]
makedepends = [
    "libstatgrab-devel",
    "ncurses-devel",
]
pkgdesc = "Bandwith Monitor NG"
license = "GPL-2.0-only"
url = "https://github.com/vgropp/bwm-ng"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c1a552b6ff48ea3e4e10110a7c188861abc4750befc67c6caaba8eb3ecf67f46"
