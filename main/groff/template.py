pkgname = "groff"
pkgver = "1.22.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--without-x", "--without-doc", "--disable-rpath"]
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["gmake", "texinfo", "perl", "bison", "ghostscript"]
makedepends = ["zlib-devel"]
pkgdesc = "GNU troff text-formatting system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/groff"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "e78e7b4cb7dec310849004fa88847c44701e8d133b5d4c13057d876c1bad0293"
# incompatible with chimerautils
options = ["!check"]

if self.profile().cross:
    hostmakedepends.append("groff")


def post_install(self):
    self.rm(self.destdir / "usr/lib", recursive=True)
    # fix some issues when encoding to utf8 man pages
    # the output chars don't match keyboard chars
    atext = (self.files_path / "site.tmac").read_bytes()
    for f in ["man", "mdoc"]:
        with open(
            self.destdir / f"usr/share/groff/site-tmac/{f}.local", "ab"
        ) as af:
            af.write(atext)


configure_gen = []
