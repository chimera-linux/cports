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
source = f"$(GNU_SITE)/make/make-{pkgver}.tar.lz"
sha256 = "8814ba072182b605d156d7589c19a43b89fc58ea479b9355146160946f8cf6e9"
hardening = ["!cfi"]  # needs figuring out hidden visibility first
# perl needs gmake to build, so tests introduce a cycle
options = ["!check"]


def post_install(self):
    self.install_link("usr/bin/gmake", "make")
