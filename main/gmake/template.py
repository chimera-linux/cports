pkgname = "gmake"
pkgver = "4.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--without-guile", "--program-prefix=g"]
hostmakedepends = ["texinfo"]
checkdepends = ["perl"]
pkgdesc = "GNU Make build tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/make"
source = f"$(GNU_SITE)/make/make-{pkgver}.tar.lz"
sha256 = "de1a441c4edf952521db30bfca80baae86a0ff1acd0a00402999344f04c45e82"
# perl needs gmake to build, so tests introduce a cycle
options = ["!check"]
