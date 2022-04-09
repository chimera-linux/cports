pkgname = "help2man"
pkgver = "1.49.1"
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
sha256 = "fd99a664ec4be9a86a0dd89719989f14f367a9c079d75d0e1d71e18a7bb51b03"
# no test suite
options = ["!check"]
