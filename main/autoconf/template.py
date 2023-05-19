pkgname = "autoconf"
pkgver = "2.71"
pkgrel = 0
build_style = "gnu_configure"
configure_env = {"M4": "/usr/bin/gm4"}
hostmakedepends = ["perl", "gm4", "texinfo"]
depends = ["cmd:awk!chimerautils", "gm4", "perl"]
pkgdesc = "Generates automatic source code configuration scripts"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/autoconf"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "431075ad0bf529ef13cb41e9042c542381103e80015686222b8a9d4abef42a1c"

configure_gen = []
