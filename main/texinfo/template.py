pkgname = "texinfo"
pkgver = "7.1"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--disable-static", "--disable-perl-xs"]
# cycle of autoconf needing this
configure_gen = []
hostmakedepends = ["perl", "ncurses-devel"]
makedepends = ["ncurses-devel"]
depends = ["perl"]
triggers = ["/usr/share/info"]
pkgdesc = "GNU Documentation System"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/texinfo"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "deeec9f19f159e046fdf8ad22231981806dac332cc372f1c763504ad82b30953"
# FIXME cfi
hardening = ["vis", "!cfi"]
