pkgname = "mc"
pkgver = "4.8.31"
pkgrel = 0
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://midnight-commander.org"
source = f"{url}/downloads/mc-{pkgver}.tar.xz"
sha256 = "24191cf8667675b8e31fc4a9d18a0a65bdc0598c2c5c4ea092494cd13ab4ab1a"
hardening = ["vis", "cfi"]
