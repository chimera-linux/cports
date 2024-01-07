pkgname = "mc"
pkgver = "4.8.30"
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
sha256 = "5ebc3cb2144b970c5149fda556c4ad50b78780494696cdf2d14a53204c95c7df"
hardening = ["vis", "cfi"]
