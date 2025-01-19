pkgname = "texinfo"
pkgver = "7.2"
pkgrel = 0
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
source = f"$(GNU_SITE)/texinfo/texinfo-{pkgver}.tar.xz"
sha256 = "0329d7788fbef113fa82cb80889ca197a344ce0df7646fe000974c5d714363a6"
hardening = ["vis", "!cfi"]
