pkgname = "texinfo"
pkgver = "6.8"
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
sha256 = "8eb753ed28bca21f8f56c1a180362aed789229bd62fff58bf8368e9beb59fec4"
