pkgname = "ncmpc"
pkgver = "0.50"
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
sha256 = "4f860f91a11090a72d580ff68b117e76a2b212be5e46cc4b986a08a1aaf4d597"
hardening = ["vis", "cfi"]
