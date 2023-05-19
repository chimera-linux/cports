pkgname = "help2man"
pkgver = "1.49.3"
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
sha256 = "4d7e4fdef2eca6afe07a2682151cea78781e0a4e8f9622142d9f70c083a2fd4f"
hardening = ["vis", "cfi"]
# no test suite
options = ["!check"]

configure_gen = []
