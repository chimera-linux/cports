pkgname = "help2man"
pkgver = "1.49.3"
pkgrel = 1
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = ["perl-locale-gettext", "texinfo"]
depends = ["perl-locale-gettext"]
pkgdesc = "GNU conversion tool to create man pages"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/help2man"
source = f"$(GNU_SITE)/help2man/help2man-{pkgver}.tar.xz"
sha256 = "4d7e4fdef2eca6afe07a2682151cea78781e0a4e8f9622142d9f70c083a2fd4f"
hardening = ["vis", "cfi"]
# no test suite
options = ["!check"]
