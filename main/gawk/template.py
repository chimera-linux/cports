pkgname = "gawk"
pkgver = "5.3.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-readline", "--disable-pma"]
# makes another test pass
make_cmd = "gmake"
hostmakedepends = ["automake", "gettext-devel", "libtool", "gmake"]
makedepends = ["libedit-readline-devel"]
pkgdesc = "GNU awk utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/gawk"
source = f"$(GNU_SITE)/gawk/gawk-{pkgver}.tar.xz"
sha256 = "ca9c16d3d11d0ff8c69d79dc0b47267e1329a69b39b799895604ed447d3ca90b"


def post_install(self):
    # hardlinks + we don't want to conflict with awk
    (self.destdir / "usr/bin/awk").unlink()
    (self.destdir / "usr/bin/gawk").unlink()
    self.install_link("usr/bin/gawk", f"gawk-{pkgver}")
