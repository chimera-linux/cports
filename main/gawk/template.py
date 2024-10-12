pkgname = "gawk"
pkgver = "5.3.1"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
    "--with-readline",
    "--disable-pma",
]
# makes another test pass
hostmakedepends = ["automake", "gettext-devel", "libtool"]
makedepends = ["libedit-readline-devel"]
pkgdesc = "GNU awk utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/gawk"
source = f"$(GNU_SITE)/gawk/gawk-{pkgver}.tar.xz"
sha256 = "694db764812a6236423d4ff40ceb7b6c4c441301b72ad502bb5c27e00cd56f78"


def post_install(self):
    # hardlinks + we don't want to conflict with awk
    self.uninstall("usr/bin/awk")
    self.uninstall("usr/bin/gawk")
    self.install_link("usr/bin/gawk", f"gawk-{pkgver}")
