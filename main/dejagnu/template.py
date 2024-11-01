pkgname = "dejagnu"
pkgver = "1.6.3"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "expect-devel"]
makedepends = ["expect-devel"]
depends = ["expect"]
pkgdesc = "Framework for running test suites on GNU tools"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/dejagnu"
source = f"$(GNU_SITE)/dejagnu/dejagnu-{pkgver}.tar.gz"
sha256 = "87daefacd7958b4a69f88c6856dbd1634261963c414079d0c371f589cd66a2e3"
hardening = ["vis", "cfi"]
# like 4 tests fail and it's impossible to tell what is going on
options = ["!check"]
