pkgname = "mc"
pkgver = "4.8.32"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://midnight-commander.org"
source = f"{url}/downloads/mc-{pkgver}.tar.xz"
sha256 = "4ddc83d1ede9af2363b3eab987f54b87cf6619324110ce2d3a0e70944d1359fe"
hardening = ["vis", "cfi"]
