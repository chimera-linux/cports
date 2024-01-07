pkgname = "groff"
pkgver = "1.23.0"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--without-x", "--without-doc", "--disable-rpath"]
configure_gen = []
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["gmake", "texinfo", "perl", "bison", "ghostscript"]
makedepends = ["zlib-devel"]
pkgdesc = "GNU troff text-formatting system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/groff"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "6b9757f592b7518b4902eb6af7e54570bdccba37a871fddb2d30ae3863511c13"
# incompatible with chimerautils
options = ["!check"]

tool_flags = {"CXXFLAGS": ["-Wno-register"]}

if self.profile().cross:
    hostmakedepends.append("groff")


def post_install(self):
    self.rm(self.destdir / "usr/lib", recursive=True)
