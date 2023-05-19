pkgname = "bison"
pkgver = "3.8.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-yacc"]
make_cmd = "gmake"
make_check_args = ["-j1"]
hostmakedepends = ["gmake", "perl", "gm4", "texinfo"]
checkdepends = ["flex", "autoconf"]
depends = ["gm4"]
pkgdesc = "GNU yacc(1) replacement"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/bison"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "9bba0214ccf7f1079c5d59210045227bcf619519840ebfa80cd3849cff5a5bf2"
# FIXME cfi
hardening = ["vis", "!cfi"]

configure_gen = []
