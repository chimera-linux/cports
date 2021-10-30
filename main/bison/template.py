pkgname = "bison"
pkgver = "3.7.6"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-yacc"]
make_check_args = ["-j1"]
hostmakedepends = ["perl", "gm4", "texinfo"]
checkdepends = ["flex"]
depends = ["gm4"]
pkgdesc = "GNU yacc(1) replacement"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/bison"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "67d68ce1e22192050525643fc0a7a22297576682bef6a5c51446903f5aeef3cf"
# FIXME
options = ["!check"]
