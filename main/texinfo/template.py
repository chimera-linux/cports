pkgname = "texinfo"
pkgver = "7.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static", "--disable-perl-xs"
]
hostmakedepends = ["perl", "ncurses-devel"]
makedepends = ["ncurses-devel"]
depends = ["perl"]
triggers = ["/usr/share/info"]
pkgdesc = "GNU Documentation System"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/texinfo"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "20744b82531ce7a04d8cee34b07143ad59777612c3695d5855f29fba40fbe3e0"
