pkgname = "ncmpc"
pkgver = "0.54"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dlirc=disabled",
    "-Dcurses=ncursesw",
    "-Dcolors=true",
    "-Dlyrics_screen=true",
    "-Dlyrics_plugin_dir=/usr/lib/ncmpc/lyrics",
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
license = "GPL-2.0-or-later"
url = "https://www.musicpd.org/clients/ncmpc"
source = f"https://www.musicpd.org/download/ncmpc/0/ncmpc-{pkgver}.tar.xz"
sha256 = "f678e6c600200af4c5d36174de4e1e82e423962c41b6f52844a25d6d1ec4cb11"
hardening = ["vis", "cfi"]
