pkgname = "texinfo"
pkgver = "6.7"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static", "--disable-perl-xs"
]
hostmakedepends = ["perl", "ncurses-devel"]
makedepends = ["ncurses-devel"]
depends = ["bsdgzip", "perl"]
triggers = ["/usr/share/info"]
pkgdesc = "GNU Documentation System"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/texinfo"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "988403c1542d15ad044600b909997ba3079b10e03224c61188117f3676b02caa"
options = ["lto"]
