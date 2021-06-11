pkgname = "texinfo"
version = "6.7"
revision = 1
build_style = "gnu_configure"
make_cmd = "bmake"
configure_args = ["--disable-static", "--disable-perl-xs"]
hostmakedepends = ["perl", "ncurses-devel"]
makedepends = ["ncurses-devel"]
depends = ["gzip", "perl"]
short_desc = "GNU Documentation System"
maintainer = "Enno Boland <gottox@voidlinux.org>"
license = "GPL-3.0-or-later"
homepage = "http://www.gnu.org/software/texinfo/"

from cbuild import sites

distfiles = [f"{sites.gnu}/{pkgname}/{pkgname}-{version}.tar.xz"]
checksum = ["988403c1542d15ad044600b909997ba3079b10e03224c61188117f3676b02caa"]

if not current.cross_build:
    configure_args.append("--enable-perl-xs")

def post_install(self):
    (self.destdir / "usr/share/info/dir").unlink(missing_ok = True)
