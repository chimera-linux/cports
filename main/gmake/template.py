pkgname = "gmake"
pkgver = "4.4.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--without-guile", "--program-prefix=g"]
checkdepends = ["perl"]
pkgdesc = "GNU Make build tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/make"
source = f"$(GNU_SITE)/make/make-{pkgver}.tar.lz"
sha256 = "8814ba072182b605d156d7589c19a43b89fc58ea479b9355146160946f8cf6e9"
hardening = ["!cfi"]  # needs figuring out hidden visibility first
# perl needs gmake to build, so tests introduce a cycle
options = ["!check"]

configure_gen = []
