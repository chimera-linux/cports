pkgname = "texinfo"
pkgver = "7.0.3"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--disable-static", "--disable-perl-xs"]
hostmakedepends = ["perl", "ncurses-devel"]
makedepends = ["ncurses-devel"]
depends = ["perl"]
triggers = ["/usr/share/info"]
pkgdesc = "GNU Documentation System"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/texinfo"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "74b420d09d7f528e84f97aa330f0dd69a98a6053e7a4e01767eed115038807bf"
# FIXME cfi
hardening = ["vis", "!cfi"]

configure_gen = []
