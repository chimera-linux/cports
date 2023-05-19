pkgname = "gm4"
pkgver = "1.4.19"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-changeword", "--enable-threads", "--program-prefix=g",
    "ac_cv_lib_error_at_line=no",
    "ac_cv_header_sys_cdefs_h=no",
]
hostmakedepends = ["texinfo"]
pkgdesc = "GNU version of UNIX m4 macro language processor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "http://www.gnu.org/software/m4"
source = f"$(GNU_SITE)/m4/m4-{pkgver}.tar.xz"
sha256 = "63aede5c6d33b6d9b13511cd0be2cac046f2e70fd0a07aa9573a04a82783af96"
# FIXME cfi - there is something wrong with oset vtable
hardening = ["vis", "!cfi"]

configure_gen = []
