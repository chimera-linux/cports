pkgname = "texinfo"
pkgver = "7.0.2"
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
sha256 = "f211ec3261383e1a89e4555a93b9d017fe807b9c3992fb2dff4871dae6da54ad"
# FIXME cfi
hardening = ["vis", "!cfi"]
