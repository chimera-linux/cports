pkgname = "gm4"
pkgver = "1.4.18"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-changeword", "--enable-threads", "--program-prefix=g",
    "ac_cv_lib_error_at_line=no",
    "ac_cv_header_sys_cdefs_h=no",
]
pkgdesc = "GNU version of UNIX m4 macro language processor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/m4"
source = f"$(GNU_SITE)/m4/m4-{pkgver}.tar.xz"
sha256 = "f2c1e86ca0a404ff281631bdc8377638992744b175afb806e25871a24a934e07"
# FIXME
options = ["!check"]

def post_install(self):
    self.rm(self.destdir / "usr/share/info", recursive = True)
