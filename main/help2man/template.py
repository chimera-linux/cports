pkgname = "help2man"
pkgver = "1.48.5"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["perl-locale-gettext", "texinfo", "gmake"]
depends = ["perl-locale-gettext"]
pkgdesc = "GNU conversion tool to create man pages"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/help2man"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "6739e4caa42e6aed3399be4387ca79399640967334e91728863b8eaa922582be"
# no test suite
options = ["!check"]
