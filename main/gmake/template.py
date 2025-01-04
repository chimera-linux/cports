pkgname = "gmake"
pkgver = "4.4.1"
pkgrel = 2
build_style = "gnu_configure"
configure_args = ["--without-guile"]
configure_gen = []
checkdepends = ["perl"]
replaces = ["bmake<=20240808-r0"]
pkgdesc = "GNU Make build tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/make"
source = f"$(GNU_SITE)/make/make-{pkgver}.tar.gz"
sha256 = "dd16fb1d67bfab79a72f5e8390735c49e3e8e70b4945a15ab1f81ddb78658fb3"
hardening = ["!cfi"]  # needs figuring out hidden visibility first
# perl needs gmake to build, so tests introduce a cycle
options = ["!check", "bootstrap"]


def post_install(self):
    self.install_link("usr/bin/gmake", "make")
