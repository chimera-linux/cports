pkgname = "gawk"
pkgver = "5.4.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-readline",
    "--disable-pma",
]
# makes another test pass
hostmakedepends = ["automake", "gettext-devel", "libtool"]
makedepends = ["libedit-readline-devel"]
pkgdesc = "GNU awk utility"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/gawk"
source = f"$(GNU_SITE)/gawk/gawk-{pkgver}.tar.xz"
sha256 = "b95e4909533b5f988c6b5e5539b3b3ddf76e7d7df02ca2e5b5b7d6f62db78e6a"
options = ["etcfiles"]


def post_install(self):
    # hardlinks + we don't want to conflict with awk
    self.uninstall("usr/bin/awk")
    self.uninstall("usr/bin/gawk")
    self.install_link("usr/bin/gawk", f"gawk-{pkgver}")
