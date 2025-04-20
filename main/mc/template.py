pkgname = "mc"
pkgver = "4.8.33"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--with-screen=ncurses", "--without-x"]
configure_gen = []  # broken m4
hostmakedepends = ["pkgconf", "perl"]
makedepends = [
    "e2fsprogs-devel",
    "glib-devel",
    "gpm-devel",
    "libssh2-devel",
    "ncurses-devel",
]
pkgdesc = "Midnight Commander"
license = "GPL-3.0-or-later"
url = "https://midnight-commander.org"
source = f"https://ftp.osuosl.org/pub/midnightcommander/mc-{pkgver}.tar.xz"
sha256 = "cae149d42f844e5185d8c81d7db3913a8fa214c65f852200a9d896b468af164c"
hardening = ["vis", "cfi"]
