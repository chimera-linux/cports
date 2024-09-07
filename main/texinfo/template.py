pkgname = "texinfo"
pkgver = "7.1.1"
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
sha256 = "31ae37e46283529432b61bee1ce01ed0090d599e606fc6a29dca1f77c76a6c82"
hardening = ["vis", "!cfi"]
