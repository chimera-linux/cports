pkgname = "findutils"
pkgver = "4.9.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--program-prefix=g",
    "ac_cv_lib_error_at_line=no",
    "ac_cv_header_sys_cdefs_h=no",
]
hostmakedepends = ["texinfo"]
pkgdesc = "GNU find utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/findutils"
source = f"$(GNU_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "a2bfb8c09d436770edc59f50fa483e785b161a3b7b9d547573cb08065fd462fe"
hardening = ["vis", "cfi"]


def post_install(self):
    # we don't want this
    self.rm(self.destdir / "usr/bin/glocate")
    self.rm(self.destdir / "usr/bin/gupdatedb")
    self.rm(self.destdir / "usr/libexec", recursive=True)
    self.rm(self.destdir / "usr/share/man/man1/glocate.1")
    self.rm(self.destdir / "usr/share/man/man1/gupdatedb.1")
    self.rm(self.destdir / "usr/share/man/man5", recursive=True)


configure_gen = []
