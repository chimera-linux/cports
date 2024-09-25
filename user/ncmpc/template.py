pkgname = "ncmpc"
pkgver = "0.51"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dlirc=disabled",
    "-Dcurses=ncursesw",
    "-Dcolors=true",
    "-Dlyrics_screen=true",
    "-Dlyrics_plugin_dir=/usr/libexec/ncmpc/lyrics",
    "-Dhtml_manual=false",
]
hostmakedepends = [
    "gettext",
    "meson",
    "pkgconf",
    "python-sphinx",
]
makedepends = [
    "fmt-devel",
    "libmpdclient-devel",
    "ncurses-devel",
    "pcre2-devel",
]
pkgdesc = "Ncurses client for the Music Player Daemon"
maintainer = "Caio Raposo <caioraposo@disroot.org>"
license = "GPL-2.0-or-later"
url = "https://www.musicpd.org/clients/ncmpc"
source = f"https://www.musicpd.org/download/ncmpc/0/ncmpc-{pkgver}.tar.xz"
sha256 = "e74be00e69bc3ed1268cafcc87274e78dfbde147f2480ab0aad8260881ec7271"
hardening = ["vis", "cfi"]
