pkgname = "gawk"
pkgver = "5.3.2"
pkgrel = 0
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
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/gawk"
source = f"$(GNU_SITE)/gawk/gawk-{pkgver}.tar.xz"
sha256 = "f8c3486509de705192138b00ef2c00bbbdd0e84c30d5c07d23fc73a9dc4cc9cc"


def post_install(self):
    # hardlinks + we don't want to conflict with awk
    self.uninstall("usr/bin/awk")
    self.uninstall("usr/bin/gawk")
    self.install_link("usr/bin/gawk", f"gawk-{pkgver}")
