pkgname = "gmake"
version = "4.3"
revision = 0
wrksrc = f"make-{version}"
build_style = "gnu_configure"
configure_args = ["--without-guile", "--program-prefix=g"]
checkdepends = ["perl"]
short_desc = "GNU Make build tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
homepage = "http://www.gnu.org/software/make"
distfiles = [f"$(GNU_SITE)/make/make-{version}.tar.lz"]
checksum = ["de1a441c4edf952521db30bfca80baae86a0ff1acd0a00402999344f04c45e82"]

def post_install(self):
    self.rm(self.destdir / "usr/share/info", recursive = True)
