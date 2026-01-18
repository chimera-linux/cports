pkgname = "ncmpc"
pkgver = "0.52"
pkgrel = 2
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
license = "GPL-2.0-or-later"
url = "https://www.musicpd.org/clients/ncmpc"
source = f"https://www.musicpd.org/download/ncmpc/0/ncmpc-{pkgver}.tar.xz"
sha256 = "3af225496fe363a8534a9780fb46ae1bd17baefd80cf4ba7430a19cddd73eb1a"
hardening = ["vis", "cfi"]
