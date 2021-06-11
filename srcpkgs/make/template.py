pkgname = "make"
version = "4.3"
revision = 3
bootstrap = True
build_style = "gnu_configure"
configure_args = ["--without-guile"]
make_cmd = "bmake"
checkdepends = ["perl"]
short_desc = "GNU Make build tool"
maintainer = "Enno Boland <gottox@voidlinux.org>"
license = "GPL-3.0-or-later"
homepage = "http://www.gnu.org/software/make"

from cbuild import sites

distfiles = [f"{sites.gnu}/make/{pkgname}-{version}.tar.lz"]
checksum = ["de1a441c4edf952521db30bfca80baae86a0ff1acd0a00402999344f04c45e82"]
patch_args = "-Np1"

def post_install(self):
    import shutil
    shutil.rmtree(self.destdir / "usr/share/info")
