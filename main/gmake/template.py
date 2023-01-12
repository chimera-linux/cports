pkgname = "gmake"
pkgver = "4.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--without-guile", "--program-prefix=g"]
checkdepends = ["perl"]
pkgdesc = "GNU Make build tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/make"
source = f"$(GNU_SITE)/make/make-{pkgver}.tar.lz"
sha256 = "48d0fc0b2a04bb50f2911c16da65723285f7f4804c74fc5a2124a3df6c5f78c4"
# FIXME: hidden visibility makes some stuff fail (not CFI)
hardening = ["!vis"]
# perl needs gmake to build, so tests introduce a cycle
options = ["!check"]
